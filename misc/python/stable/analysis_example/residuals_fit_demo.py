#!/usr/bin/env python3
"""
Residuals Analysis Demo
Educational demonstration of residual analysis from first principles
"""

import numpy as np
import matplotlib.pyplot as plt


def generate_data(n_points=100, noise=3.0, true_slope=2.0, true_intercept=5.0):
    """
    Generate synthetic linear data with Gaussian noise

    Formula: y = slope * x + intercept + noise
    """
    np.random.seed(42)
    x = np.linspace(0, 10, n_points)
    y = true_slope * x + true_intercept + np.random.normal(0, noise, n_points)
    return x, y


def fit_linear_model(x, y):
    """
    Fit linear model using least squares (analytical solution)

    This is the closed-form solution to minimize sum of squared residuals:
    slope = covariance(x,y) / variance(x)
    intercept = mean(y) - slope * mean(x)
    """
    # Calculate means
    x_mean = np.mean(x)
    y_mean = np.mean(y)

    # Calculate slope using covariance/variance formula
    numerator = np.sum((x - x_mean) * (y - y_mean))
    denominator = np.sum((x - x_mean) ** 2)
    slope = numerator / denominator

    # Calculate intercept
    intercept = y_mean - slope * x_mean

    return slope, intercept


def calculate_residuals(x, y, slope, intercept):
    """
    Calculate residuals from first principles

    Residual = Observed - Predicted

    Residuals tell us:
    - How much each point deviates from the model
    - Whether the model assumptions are valid
    - If there are patterns we're missing
    """
    predictions = slope * x + intercept
    residuals = y - predictions
    return residuals


def calculate_fit_statistics(residuals, n_params=2):
    """
    Calculate key statistics about the fit quality

    Parameters:
    - n_params: number of fitted parameters (slope + intercept = 2)
    """
    n_points = len(residuals)
    degrees_of_freedom = n_points - n_params

    # Sum of squared residuals (SSR) - what we minimize
    ssr = np.sum(residuals ** 2)

    # Mean squared error (MSE) - average squared residual
    mse = ssr / degrees_of_freedom

    # Root mean squared error (RMSE) - in same units as y
    rmse = np.sqrt(mse)

    # Standard deviation of residuals
    residual_std = np.std(residuals, ddof=n_params)

    return {
        'ssr': ssr,
        'mse': mse,
        'rmse': rmse,
        'residual_std': residual_std,
        'degrees_of_freedom': degrees_of_freedom
    }


def check_residual_patterns(residuals):
    """
    Check for common patterns in residuals that indicate problems

    Good residuals should be:
    1. Centered around zero (mean ~ 0)
    2. Randomly scattered (no patterns)
    3. Roughly normally distributed
    4. Constant variance (homoscedastic)
    """
    checks = {
        'mean': np.mean(residuals),
        'median': np.median(residuals),
        'std': np.std(residuals),
        'min': np.min(residuals),
        'max': np.max(residuals)
    }

    # Check if mean is close to zero (should be for unbiased fit)
    checks['mean_near_zero'] = abs(checks['mean']) < 0.1 * checks['std']

    # Count outliers (beyond 2 standard deviations)
    outliers = np.abs(residuals) > 2 * checks['std']
    checks['n_outliers'] = np.sum(outliers)
    checks['outlier_fraction'] = checks['n_outliers'] / len(residuals)

    return checks


def plot_residuals_analysis(x, y, slope, intercept, residuals, stats):
    """
    Create comprehensive visualization of residuals
    """
    predictions = slope * x + intercept

    fig = plt.figure(figsize=(14, 10))

    # Plot 1: Original data with fitted line
    ax1 = plt.subplot(2, 3, 1)
    ax1.scatter(x, y, alpha=0.6, label='Data', color='blue')
    ax1.plot(x, predictions, 'r-', linewidth=2,
             label=f'Fit: y = {slope:.2f}x + {intercept:.2f}')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_title('Data and Fitted Model')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Plot 2: Residuals vs x (check for patterns)
    ax2 = plt.subplot(2, 3, 2)
    ax2.scatter(x, residuals, alpha=0.6, color='green')
    ax2.axhline(y=0, color='r', linestyle='--', linewidth=1, label='Zero line')
    ax2.axhline(y=2*stats['residual_std'], color='orange',
                linestyle=':', linewidth=1, label='±2σ')
    ax2.axhline(y=-2*stats['residual_std'], color='orange',
                linestyle=':', linewidth=1)
    ax2.set_xlabel('x')
    ax2.set_ylabel('Residuals')
    ax2.set_title('Residuals vs x\n(Should show no pattern)')
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    # Plot 3: Residuals vs fitted values (check for heteroscedasticity)
    ax3 = plt.subplot(2, 3, 3)
    ax3.scatter(predictions, residuals, alpha=0.6, color='purple')
    ax3.axhline(y=0, color='r', linestyle='--', linewidth=1)
    ax3.axhline(y=2*stats['residual_std'], color='orange',
                linestyle=':', linewidth=1)
    ax3.axhline(y=-2*stats['residual_std'], color='orange',
                linestyle=':', linewidth=1)
    ax3.set_xlabel('Fitted values')
    ax3.set_ylabel('Residuals')
    ax3.set_title('Residuals vs Fitted\n(Check constant variance)')
    ax3.grid(True, alpha=0.3)

    # Plot 4: Histogram of residuals (check normality)
    ax4 = plt.subplot(2, 3, 4)
    ax4.hist(residuals, bins=20, alpha=0.7, color='teal', edgecolor='black')
    ax4.axvline(x=0, color='r', linestyle='--', linewidth=2, label='Zero')
    ax4.set_xlabel('Residual value')
    ax4.set_ylabel('Frequency')
    ax4.set_title('Distribution of Residuals\n(Should be roughly normal)')
    ax4.legend()
    ax4.grid(True, alpha=0.3)

    # Plot 5: Q-Q plot (quantile-quantile, check normality)
    ax5 = plt.subplot(2, 3, 5)
    sorted_residuals = np.sort(residuals)
    n = len(residuals)
    theoretical_quantiles = np.random.normal(0, stats['residual_std'], n)
    theoretical_quantiles = np.sort(theoretical_quantiles)

    ax5.scatter(theoretical_quantiles, sorted_residuals, alpha=0.6, color='brown')
    # Add diagonal line for perfect normal distribution
    min_val = min(theoretical_quantiles.min(), sorted_residuals.min())
    max_val = max(theoretical_quantiles.max(), sorted_residuals.max())
    ax5.plot([min_val, max_val], [min_val, max_val], 'r--', linewidth=2,
             label='Perfect normal')
    ax5.set_xlabel('Theoretical quantiles')
    ax5.set_ylabel('Sample quantiles')
    ax5.set_title('Q-Q Plot\n(Points should follow red line)')
    ax5.legend()
    ax5.grid(True, alpha=0.3)

    # Plot 6: Statistics summary (text)
    ax6 = plt.subplot(2, 3, 6)
    ax6.axis('off')

    summary_text = f"""
Fit Statistics:
━━━━━━━━━━━━━━━━━━━━━━━━━
RMSE: {stats['rmse']:.4f}
Residual Std: {stats['residual_std']:.4f}
Sum Squared Residuals: {stats['ssr']:.2f}
Degrees of Freedom: {stats['degrees_of_freedom']}

Residual Properties:
━━━━━━━━━━━━━━━━━━━━━━━━━
Mean: {np.mean(residuals):.4f}
  (should be ≈ 0)
Median: {np.median(residuals):.4f}
Range: [{np.min(residuals):.2f}, {np.max(residuals):.2f}]

Good Fit Indicators:
━━━━━━━━━━━━━━━━━━━━━━━━━
✓ Mean near zero
✓ Random scatter in plots
✓ Normal distribution
✓ Constant variance
    """

    ax6.text(0.1, 0.9, summary_text, transform=ax6.transAxes,
             fontsize=10, verticalalignment='top',
             fontfamily='monospace',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))

    plt.tight_layout()
    return fig


def demonstrate_bad_fit(x):
    """
    Create example of poor fit to show what bad residuals look like

    Fit a linear model to obviously non-linear (quadratic) data
    """
    # Generate quadratic data
    true_coeffs = [0.5, 2.0, 5.0]  # ax^2 + bx + c
    y_quad = true_coeffs[0] * x**2 + true_coeffs[1] * x + true_coeffs[2]
    y_quad += np.random.normal(0, 2.0, len(x))  # Add some noise

    # Fit linear model (wrong model!)
    slope, intercept = fit_linear_model(x, y_quad)
    residuals = calculate_residuals(x, y_quad, slope, intercept)

    return y_quad, slope, intercept, residuals


def main():
    print("=" * 60)
    print("RESIDUALS ANALYSIS FROM FIRST PRINCIPLES")
    print("=" * 60)

    # Part 1: Good fit example
    print("\n1. Generating data and fitting model...")
    x, y = generate_data(n_points=100, noise=3.0, true_slope=2.0, true_intercept=5.0)
    slope, intercept = fit_linear_model(x, y)

    print(f"   Fitted model: y = {slope:.4f}*x + {intercept:.4f}")
    print(f"   True model:   y = 2.0000*x + 5.0000")

    # Part 2: Calculate residuals
    print("\n2. Calculating residuals from first principles...")
    residuals = calculate_residuals(x, y, slope, intercept)
    print(f"   Number of residuals: {len(residuals)}")

    # Part 3: Analyze residuals
    print("\n3. Analyzing residual statistics...")
    stats = calculate_fit_statistics(residuals)
    print(f"   RMSE: {stats['rmse']:.4f}")
    print(f"   Residual Std Dev: {stats['residual_std']:.4f}")

    checks = check_residual_patterns(residuals)
    print("\n4. Checking residual patterns...")
    print(f"   Mean residual: {checks['mean']:.4f} (should be ≈ 0)")
    print(f"   Mean near zero? {checks['mean_near_zero']}")
    print(f"   Outliers: {checks['n_outliers']} ({checks['outlier_fraction']*100:.1f}%)")

    # Part 4: Visualize
    print("\n5. Creating visualizations...")
    fig = plot_residuals_analysis(x, y, slope, intercept, residuals, stats)
    plt.savefig('residuals_analysis_good.png', dpi=150, bbox_inches='tight')
    print("   Saved: residuals_analysis_good.png")

    # Part 5: Demonstrate bad fit
    print("\n6. Demonstrating BAD fit (linear model on quadratic data)...")
    y_quad, slope_bad, intercept_bad, residuals_bad = demonstrate_bad_fit(x)
    stats_bad = calculate_fit_statistics(residuals_bad)

    fig2 = plot_residuals_analysis(x, y_quad, slope_bad, intercept_bad,
                                    residuals_bad, stats_bad)
    plt.savefig('residuals_analysis_bad.png', dpi=150, bbox_inches='tight')
    print("   Saved: residuals_analysis_bad.png")
    print("   Notice the clear PATTERN in residuals - this indicates")
    print("   the linear model is not appropriate for this data!")

    print("\n" + "=" * 60)
    print("KEY INSIGHTS:")
    print("=" * 60)
    print("Good residuals: Random scatter, centered at zero, no patterns")
    print("Bad residuals:  Clear patterns, systematic deviations")
    print("=" * 60)

    plt.show()


if __name__ == "__main__":
    main()
