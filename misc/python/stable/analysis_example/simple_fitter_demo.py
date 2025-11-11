#!/usr/bin/env python3
"""
Simple Linear Regression Fitter Demo
Educational demonstration of gradient descent optimization
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter


def generate_data(n_points=50, noise=5.0, true_slope=2.5, true_intercept=10.0):
    """
    Generate synthetic linear data with noise

    Formula: y = slope * x + intercept + noise
    """
    np.random.seed(42)  # For reproducible results
    x = np.linspace(0, 10, n_points)
    y = true_slope * x + true_intercept + np.random.normal(0, noise, n_points)
    return x, y


def predict(x, slope, intercept):
    """Make predictions using the linear model: y = slope * x + intercept"""
    return slope * x + intercept


def compute_loss(x, y, slope, intercept):
    """
    Compute Mean Squared Error (MSE) loss

    MSE = average of (actual - predicted)^2
    This tells us how well our line fits the data
    """
    predictions = predict(x, slope, intercept)
    return np.mean((y - predictions) ** 2)


def fit_linear_regression(x, y, learning_rate=0.01, n_iterations=100):
    """
    Fit linear regression using gradient descent

    Gradient descent is an optimization algorithm that:
    1. Starts with random parameters (slope=0, intercept=0)
    2. Calculates how much to adjust them to reduce error
    3. Takes small steps in the right direction
    4. Repeats until we find the best fit
    """
    # Start with slope=0 and intercept=0
    slope = 0.0
    intercept = 0.0

    # Track how parameters and loss change over time
    loss_history = []
    slope_history = []
    intercept_history = []

    # Gradient descent loop
    for i in range(n_iterations):
        # Calculate current predictions and error
        n = len(x)
        predictions = predict(x, slope, intercept)
        error = y - predictions

        # Calculate gradients (how much to change each parameter)
        # These formulas come from calculus (partial derivatives of MSE)
        gradient_slope = -(2/n) * np.sum(x * error)
        gradient_intercept = -(2/n) * np.sum(error)

        # Update parameters by taking a small step in the direction of lower error
        slope = slope - learning_rate * gradient_slope
        intercept = intercept - learning_rate * gradient_intercept

        # Record the current loss and parameters
        loss = compute_loss(x, y, slope, intercept)
        loss_history.append(loss)
        slope_history.append(slope)
        intercept_history.append(intercept)

        # Print progress every 50 iterations
        if (i + 1) % 50 == 0:
            print(f"Iteration {i+1}: Loss = {loss:.4f}, Slope = {slope:.4f}, Intercept = {intercept:.4f}")

    return slope, intercept, loss_history, slope_history, intercept_history


def plot_results(x, y, slope, intercept, loss_history):
    """Create visualization of the fit and training process"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Left plot: Data and fitted line
    ax1.scatter(x, y, alpha=0.6, label='Data points', color='blue')
    predictions = predict(x, slope, intercept)
    ax1.plot(x, predictions, 'r-', linewidth=2, label=f'Fit: y = {slope:.2f}x + {intercept:.2f}')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_title('Linear Regression Fit')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Right plot: Loss over iterations
    ax2.plot(loss_history, linewidth=2, color='green')
    ax2.set_xlabel('Iteration')
    ax2.set_ylabel('Loss (Mean Squared Error)')
    ax2.set_title('How Error Decreases During Training')
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    return fig


def create_animation(x, y, slope_history, intercept_history, loss_history, filename='linear_regression_animation.gif'):
    """
    Create an animated GIF showing how the fitted line evolves during training
    """
    print(f"Creating animation with {len(slope_history)} frames...")

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Set up the left plot (data and fitted line)
    ax1.scatter(x, y, alpha=0.6, color='blue', label='Data points')
    line, = ax1.plot([], [], 'r-', linewidth=2, label='Fitted line')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_xlim(x.min() - 1, x.max() + 1)
    ax1.set_ylim(y.min() - 5, y.max() + 5)
    ax1.set_title('Linear Regression Training Progress')
    ax1.grid(True, alpha=0.3)
    ax1.legend()

    # Set up the right plot (loss over time)
    ax2.set_xlabel('Iteration')
    ax2.set_ylabel('Loss (Mean Squared Error)')
    ax2.set_title('Loss Decreasing Over Time')
    ax2.set_xlim(0, len(loss_history))
    ax2.set_ylim(0, max(loss_history) * 1.1)
    ax2.grid(True, alpha=0.3)
    loss_line, = ax2.plot([], [], linewidth=2, color='green')

    # Text annotation for iteration number
    iteration_text = ax1.text(0.02, 0.98, '', transform=ax1.transAxes,
                             verticalalignment='top', fontsize=10,
                             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    def init():
        line.set_data([], [])
        loss_line.set_data([], [])
        iteration_text.set_text('')
        return line, loss_line, iteration_text

    def animate(frame):
        # Sample frames to make animation smoother and smaller
        # Show every Nth frame to reduce file size
        step = max(1, len(slope_history) // 100)  # Max 100 frames
        i = min(frame * step, len(slope_history) - 1)

        # Update the fitted line
        slope = slope_history[i]
        intercept = intercept_history[i]
        y_pred = predict(x, slope, intercept)
        line.set_data(x, y_pred)

        # Update the loss plot
        loss_line.set_data(range(i+1), loss_history[:i+1])

        # Update text
        iteration_text.set_text(f'Iteration: {i+1}\ny = {slope:.2f}x + {intercept:.2f}\nLoss: {loss_history[i]:.2f}')

        return line, loss_line, iteration_text

    # Calculate number of frames
    step = max(1, len(slope_history) // 100)
    n_frames = min(100, len(slope_history) // step)

    # Create animation
    anim = FuncAnimation(fig, animate, init_func=init, frames=n_frames,
                        interval=50, blit=True, repeat=True)

    # Save as GIF
    writer = PillowWriter(fps=20)
    anim.save(filename, writer=writer)
    print(f"Animation saved to {filename}")

    plt.close(fig)


def main():
    x, y = generate_data(n_points=50, noise=5.0, true_slope=2.5, true_intercept=10.0)

    learning_rate = 0.01
    n_iterations = 2000
    slope, intercept, loss_history, slope_history, intercept_history = fit_linear_regression(
        x, y, learning_rate=learning_rate, n_iterations=n_iterations
    )

    # Step 3: Show results
    print("\n3. Final Results:")
    print(f"   Fitted equation: y = {slope:.4f}*x + {intercept:.4f}")
    print(f"   Final loss: {loss_history[-1]:.4f}")
    print(f"   True equation:  y = 2.5000*x + 10.0000")
    print(f"   Error in slope: {abs(slope - 2.5):.4f}")
    print(f"   Error in intercept: {abs(intercept - 10.0):.4f}")

    # Step 4: Visualize
    print("\n4. Creating visualization...")
    fig = plot_results(x, y, slope, intercept, loss_history)
    plt.savefig('linear_regression_fit.png', dpi=150, bbox_inches='tight')

    # Step 5: Create animation
    print("\n5. Creating animation of training progress...")
    create_animation(x, y, slope_history, intercept_history, loss_history)

    plt.show()


if __name__ == "__main__":
    main()
