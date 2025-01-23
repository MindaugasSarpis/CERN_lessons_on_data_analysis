import matplotlib.pyplot as plt
import numpy as np

def format_fig(width = 16, height = 9):
    fig, ax = plt.subplots(figsize=(width, height))

    # Dynamically adjust font sizes and label padding based on figure size
    font_size = width * 1.5  # Scale font size by figure width
    label_pad = width * 0.5  # Scale label padding by figure width
    tick_label_size = width * 1.2  # Scale tick label size

    # Customize labels and tick marks with dynamic font sizes
    ax.set_xlabel("Value", fontsize=font_size, loc="right")
    ax.set_ylabel("Frequency", fontsize=font_size, labelpad=label_pad, loc="top")

    # Customize tick params with dynamic sizes
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


    return fig, ax 

def plot_hist(data, n_bins = None, axis_padding = None, width=16, height=9, xlow=0, xup=21):

    fig, ax = format_fig(width, height)
    
    # Set ticks on x and y axis
    
    if n_bins is None:
        n_bins = xup - xlow + 1
    
    # Plot the histogram and capture the bin heights
    n, bins, patches = ax.hist(
        data, bins=n_bins, edgecolor="black", linewidth=1.2, range = (np.floor(xlow), np.floor(xup)+1), 
    )

    x_range = np.floor(xup) - np.floor(xlow)
    xtics = np.linspace(np.floor(xlow), np.floor(xup), int(x_range) + 1)

    ax.set_xticks(xtics)
    ax.set_xlim(np.floor(xlow), np.floor(xup))

    print(bins)
    # Automatically set the y-axis limit based on the histogram data
    max_height = np.max(n)

    divisor = 1
    # Round y_limit to the nearest 500 (or other suitable rounding)
    y_limit = (
        np.ceil(max_height * 1.1 / divisor) * divisor
    )  # Rounds up to the nearest 500

    # Set the y-axis limit with the rounded value
    ax.set_ylim(0, y_limit)

    # Set y-ticks with rounded and nicely spaced values
    # y_ticks = np.linspace(0, y_limit, 11)  # 11 evenly spaced ticks from 0 to y_limit
    # ax.set_yticks(y_ticks)

    # Save the figure
    plt.savefig("Important_Histo.pdf")
    plt.show()

    return n, bins, patches

from collections import Counter


def grade_chart(data):
    
    grades = list(range(0, 11))  # Grades from 0 to 10

    # Count occurrences of each grade and ensure all grades from 0 to 10 are included
    counts = Counter(data)
    full_grade_counts = [counts.get(grade, 0) for grade in grades]  # Convert to list of counts

    fig, ax = format_fig()

    # Create the bar chart
    plt.bar(grades, full_grade_counts, color='skyblue', edgecolor='black')

    # Labeling the axes and adding a title
    plt.xlabel('Grades')
    plt.ylabel('Number of Students')

    # Setting the ticks on the x-axis to show each grade
    plt.xticks(grades)

    # Display the plot
    plt.show()
