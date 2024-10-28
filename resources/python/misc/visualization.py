import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# Set up the figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Generate the x and y data
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
x, y = np.meshgrid(x, y)

# Initial z data for a sine wave
z = np.sin(np.sqrt(x**2 + y**2))

# Plot the initial surface
surf = ax.plot_surface(x, y, z, cmap='viridis')

# Set axis limits
ax.set_zlim([-1, 1])

# Animation function: This updates the z data to create a wave effect
def update(frame):
    z = np.sin(np.sqrt(x**2 + y**2) - frame / 10.0)  # Update z to make the wave move
    ax.clear()  # Clear the previous frame
    surf = ax.plot_surface(x, y, z, cmap='viridis')  # Plot updated surface
    ax.set_zlim([-1, 1])  # Maintain z-axis limits
    return surf,

# Create the animation
ani = FuncAnimation(fig, update, frames=1000, interval=5)

# Display the animated plot
plt.show()