"""Assemble captured frames into animated GIF (+ WebP if PIL supports it).
  python3 make-gif.py <frames_dir> <out_base> --mode loop --overlap 15 --fps 12.5 --widths 1280,960
  python3 make-gif.py <frames_dir> <out_base> --mode intro --fade 8 ...
loop : crossfade the last <overlap> frames into the first <overlap> (seamless seam), drop the tail
intro: multiply the last <fade> frames toward black so the restart reads as a deliberate replay
"""
import argparse, subprocess, sys, os, glob, shutil
from PIL import Image
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument('frames'); ap.add_argument('out_base')
ap.add_argument('--mode', default='loop'); ap.add_argument('--overlap', type=int, default=15)
ap.add_argument('--fade', type=int, default=8); ap.add_argument('--fps', type=float, default=12.5)
ap.add_argument('--widths', default='1280,960'); ap.add_argument('--webp', action='store_true')
ap.add_argument('--dither', default='none')      # none | bayer:bayer_scale=5 | sierra2_4a
ap.add_argument('--colors', type=int, default=128)
ap.add_argument('--black', type=int, default=0)  # clamp pixels below this to pure black (flat bg → small GIF)
ap.add_argument('--keep', action='store_true'); ap.add_argument('--webp-q', type=int, default=75)
ap.add_argument('--gif-fps', type=float, default=0)   # resample GIF to this rate (GIF max ≈ 50 fps: 20 ms delays)
ap.add_argument('--webp-widths', default=''); ap.add_argument('--webp-fps', type=float, default=0)          # widths for WebP (default: same as --widths)
a = ap.parse_args()

files = sorted(glob.glob(os.path.join(a.frames, 'f*.png')))
n = len(files)
tmp = a.out_base + '.frames'
shutil.rmtree(tmp, ignore_errors=True); os.makedirs(tmp)
load = lambda f: np.asarray(Image.open(f).convert('RGB'), dtype=np.float32)
def knee(img):
    # Flatten the near-black background (faint ambient dust + gradient) to pure
    # black with a soft knee on the brightest channel — hue is preserved, and
    # the flat background is what makes the GIF's LZW compress. Sphere/fibers
    # are far above the knee.
    if not a.black: return img
    m = img.max(axis=2, keepdims=True)
    return img * np.clip((m - a.black) / 24.0, 0, 1)
save = lambda img, f: Image.fromarray(np.clip(img, 0, 255).astype(np.uint8)).save(f)

if a.mode == 'loop':
    K = a.overlap; keep = n - K
    for i in range(keep):
        if i < K:
            w = (i + 1) / (K + 1)                       # ramp: tail fades out, head fades in
            save(knee((1 - w) * load(files[i]) + w * load(files[keep + i])), f'{tmp}/f{i:04d}.png')
        else:
            save(knee(load(files[i])), f'{tmp}/f{i:04d}.png')
else:
    F = a.fade; keep = n
    for i in range(n):
        if i >= n - F:
            w = 1 - (i - (n - F) + 1) / F                # → 0 on the last frame
            save(knee(load(files[i])) * (w * w), f'{tmp}/f{i:04d}.png')
        else:
            save(knee(load(files[i])), f'{tmp}/f{i:04d}.png')
print(f'{a.mode}: {keep} frames @ {a.fps} fps = {keep / a.fps:.1f}s')

for wpx in [int(x) for x in a.widths.split(',')]:
    out = f'{a.out_base}-{wpx}.gif'
    resample = f'fps={a.gif_fps},' if a.gif_fps else ''
    vf = (f'{resample}scale={wpx}:-1:flags=lanczos,split[s0][s1];'
          f'[s0]palettegen=max_colors={a.colors}:stats_mode=diff[p];'
          f'[s1][p]paletteuse=dither={a.dither}:diff_mode=rectangle')
    subprocess.run(['ffmpeg', '-y', '-hide_banner', '-loglevel', 'error', '-framerate', str(a.fps),
                    '-i', f'{tmp}/f%04d.png', '-vf', vf, '-loop', '0', out], check=True)
    print(f'  {out}  {os.path.getsize(out) / 1e6:.1f} MB')
    if a.webp and (not a.webp_widths or str(wpx) in a.webp_widths.split(',')):
        try:
            def rz(i):
                im = Image.open(f'{tmp}/f{i:04d}.png').convert('RGB')
                return im.resize((wpx, round(im.height * wpx / im.width)), Image.LANCZOS)
            wf = a.webp_fps or a.fps
            step = a.fps / wf                        # subsample the capture rate to the WebP rate
            idx = sorted({int(round(j * step)) for j in range(int(keep / step))} & set(range(keep)))
            frames = [rz(i) for i in idx]            # resized on load — keeps memory to ~1.5 MB/frame
            outw = f'{a.out_base}-{wpx}.webp'
            frames[0].save(outw, save_all=True, append_images=frames[1:], duration=int(round(1000 / wf)),
                           loop=0, quality=a.webp_q, method=4)
            print(f'  {outw}  {os.path.getsize(outw) / 1e6:.1f} MB')
        except Exception as e:
            print('  webp skipped:', e)
if not a.keep: shutil.rmtree(tmp)
