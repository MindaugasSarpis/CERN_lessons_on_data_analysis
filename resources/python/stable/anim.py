import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import pandas as pd 
def plot_hist_animation(data, xlow=0, xup=21, width=16, height=9):
    fig, ax = plt.subplots(figsize=(width, height))

    # Set labels and ticks
    font_size = width * 1.5
    label_pad = width * 0.5
    tick_label_size = width * 1.2

    ax.set_xlabel("Value", fontsize=font_size, loc="right")
    ax.set_ylabel("Frequency", fontsize=font_size, labelpad=label_pad, loc="top")
    ax.tick_params(
        axis="both",
        labelsize=tick_label_size,
        size=width * 0.8,
        width=width * 0.2,
        top=True,
        right=True,
        direction="inout",
    )
    [ax.spines[i].set_linewidth(2) for i in ["top", "right", "left", "bottom"]]

    # Set x-axis ticks and limits
    bins = np.arange(xlow, xup + 2, 1)  # Bin edges from xlow to xup+1
    ax.set_xticks(np.arange(xlow, xup + 1, 1))
    ax.set_xlim(xlow, xup + 1)

    # Compute the total histogram data for y-axis limits
    n_total, _ = np.histogram(data, bins=bins, range=(xlow, xup + 1))
    y_limit = np.ceil(np.max(n_total) * 1.1)
    ax.set_ylim(0, y_limit)
    ax.set_yticks(np.arange(0, y_limit + 1, max(1, int(y_limit // 10))))

    # Initialize the bars with zero height
    bar_container = ax.bar(
        bins[:-1], np.zeros_like(n_total), width=1.0, edgecolor="black", align="edge"
    )

    # Animation function
    def animate(frame):
        # Update the histogram with data up to the current frame
        current_data = data[:frame + 1]
        n, _ = np.histogram(current_data, bins=bins, range=(xlow, xup + 1))
        for rect, h in zip(bar_container.patches, n):
            rect.set_height(h)
        return bar_container.patches

    total_frames = 10000
    anim = FuncAnimation(
        fig, animate, frames=total_frames, interval=50, blit=True
    )
    anim.save('animated_histogram.gif', writer='pillow')

    plt.show()

# Example usage:
data = pd.read_csv('../../data/quiz_1.csv')
plot_hist_animation(data, xlow=14, xup=22)
