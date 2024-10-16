import matplotlib.pyplot as plt
import numpy as np


def super_function(dist1, n_bins,):

    # Set the desired aspect ratio, e.g., 3:4
    aspect_ratio = (1, 1)  # width:height

    # Dynamically calculate the figure size while maintaining the aspect ratio
    fig_width = 9  # Adjust this width to suit your needs
    fig_height = fig_width * aspect_ratio[1] / aspect_ratio[0]
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))

    # Dynamically adjust font sizes and label padding based on figure size
    font_size = fig_width * 1.5  # Scale font size by figure width
    label_pad = fig_width * 0.5  # Scale label padding by figure width
    tick_label_size = fig_width * 1.2  # Scale tick label size

    # Customize labels and tick marks with dynamic font sizes
    ax.set_xlabel('Value', fontsize=font_size, loc='right')
    ax.set_ylabel('Frequency', fontsize=font_size, labelpad=label_pad, loc='top')

    # Customize tick params with dynamic sizes
    ax.tick_params(axis='both', labelsize=tick_label_size, size=fig_width * 0.8, width=fig_width * 0.3, top=True, right=True, direction='inout')
    [ax.spines[i].set_linewidth(fig_width * 0.2) for i in ['top', 'right', 'left', 'bottom']]

    # Set ticks on x and y axis
    ax.set_xticks([-5, -2.5, 0, 2.5, 5])
    ax.set_xlim(-5, 5)
    # Plot the histogram and capture the bin heights
    n, bins, patches = ax.hist(dist1, bins=n_bins)

    # Automatically set the y-axis limit based on the histogram data
    max_height = np.max(n)

    # Round y_limit to the nearest 500 (or other suitable rounding)
    y_limit = np.ceil(max_height*1.1 / 500.0) * 500  # Rounds up to the nearest 500

    # Set the y-axis limit with the rounded value
    ax.set_ylim(0, y_limit)

    # Set y-ticks with rounded and nicely spaced values
    y_ticks = np.linspace(0, y_limit, 11)  # 11 evenly spaced ticks from 0 to y_limit
    ax.set_yticks(y_ticks)

    # Save the figure
    plt.savefig('Important_Histo.pdf')
    plt.show()