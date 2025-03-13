import matplotlib.pyplot as plt
from matplotlib.colors import LightSource
import copy

def plot_route(steps, mars_map, scale, label):
    #Showing the route

    # Extract x, y coordinates from the path
    path_rows, path_cols = zip(*steps)

    # Convert row, col indices to real-world coordinates
    path_x = [col * scale for col in path_cols]
    path_y = [(mars_map.shape[0] - row) * scale for row in path_rows]  # Flip y-axis

    # Plot the heightmap
    fig, ax = plt.subplots()
    cmap = copy.copy(plt.cm.get_cmap('autumn'))
    cmap.set_under(color='black')

    ls = LightSource(315, 45)
    rgb = ls.shade(mars_map, cmap=cmap, vmin=0, vmax=mars_map.max(), vert_exag=2, blend_mode='hsv')

    im = ax.imshow(rgb, extent=[0, mars_map.shape[1] * scale, 0, mars_map.shape[0] * scale],
                interpolation='nearest', origin='upper')

    # Plot the path
    ax.plot(path_x, path_y, marker="o", color="blue", linewidth=1, markersize=1, label="Robot Path")

    # Labels and legend
    title = "Mars Surface with Robot Path using "+label
    plt.title(title)
    plt.xlabel("x (m)")
    plt.ylabel("y (m)")
    plt.legend()
    plt.show()