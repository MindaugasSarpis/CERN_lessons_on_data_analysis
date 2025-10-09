import os

# Create folder to hold output
output_dir = "dash_naming_examples"
os.makedirs(output_dir, exist_ok=True)

# Various dash and separator characters
separators = [
    "-",        # Hyphen-minus (standard, safe)
    "_",        # Underscore (safe)
    " ",        # Space (risky)
    "–",        # En dash (U+2013)
    "—",        # Em dash (U+2014)
    "‒",        # Figure dash (U+2012)
    "−",        # Minus sign (U+2212)
    "﹣",        # Small hyphen-minus (U+FE63)
    "－",        # Fullwidth hyphen-minus (U+FF0D)
    "‾",        # Overline (U+203E)
    "―",        # Horizontal bar (U+2015)
    "⸺",        # Two-em dash (U+2E3A)
    "⸻",        # Three-em dash (U+2E3B)
]

base_names = ["data", "analysis", "report", "test", "final", "draft"]

count = 0
for sep in separators:
    for i in range(4):  # 4 files per separator, total ≈ 52
        name = f"{base_names[i]}{sep}{base_names[-(i+1)]}_{count+1:02d}.txt"
        file_path = os.path.join(output_dir, name)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"Example file using separator: {repr(sep)}\n")
        print("Created:", name)
        count += 1
        if count >= 50:
            break
    if count >= 50:
        break

print(f"\n✅ Created {count} files in '{output_dir}' with varied dash/underscore types.")

