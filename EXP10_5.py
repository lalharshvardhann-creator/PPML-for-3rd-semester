# WAP to draw the 3D-plot.
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a new figure
fig = plt.figure()

# Add a 3D subplot to the figure
ax = fig.add_subplot(111, projection='3d')

# Define X-axis values
x = [1, 2, 3, 4, 5]

# Define Y-axis values
y = [5, 6, 7, 8, 9]

# Define Z-axis values
z = [2, 3, 3, 3, 2]

# Plot the points in 3D using a red color
ax.scatter(x, y, z, color='r', label="3D Points")

# Set the title of the graph
ax.set_title("3D Scatter Plot")

# Label the X-axis
ax.set_xlabel("X-axis")

# Label the Y-axis
ax.set_ylabel("Y-axis")

# Label the Z-axis
ax.set_zlabel("Z-axis")

# Display the legend
plt.legend()

# Display the 3D plot
plt.show()
