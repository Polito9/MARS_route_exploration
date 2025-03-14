import numpy as np
import matplotlib.pyplot as plt

height_map = np.load("crater_map.npy")

visited = set()

minimum_height = 200

def meters_to_indices(x, y, scale):
    """
    Convierte coordenadas (x, y) en metros a índices (i, j) de la matriz.
    """
    return int(y // scale), int(x // scale)

def get_neighbors(i, j):
    """
    Devuelve las coordenadas de los 8 vecinos de la celda (i, j).
    """
    return [
        (i-1, j-1), (i-1, j), (i-1, j+1),
        (i, j-1),          (i, j+1),
        (i+1, j-1), (i+1, j), (i+1, j+1)
    ]

def greedy_search(height_map, start_x, start_y, scale, max_height_diff=2.0):
    global minimum_height
    """
    Realiza greedy desde la posición inicial (start_x, start_y).
    Devuelve la trayectoria y la altura más baja alcanzada.
    """
    # Convertir coordenadas en metros a índices de la matriz
    i, j = start_x, start_y
    print(i, j)
    # Inicializar la trayectoria y la altura actual
    trajectory = [(i, j)]
    current_height = height_map[i, j]
    while True:
        neighbors = get_neighbors(i, j)
        valid_neighbors = []
        
        # Revisar los 8 vecinos
        for ni, nj in neighbors:
            # Verificar si el vecino está dentro de los límites del mapa
            if 0 <= ni < height_map.shape[0] and 0 <= nj < height_map.shape[1]:
                neighbor_height = height_map[ni, nj]
                # Verificar si el vecino es válido (diferencia de altura <= max_height_diff)
                if neighbor_height != -1 and abs(neighbor_height - current_height) <= max_height_diff and (ni, nj) not in visited:
                    valid_neighbors.append((ni, nj, neighbor_height))
        
        # Si no hay vecinos válidos, terminar la búsqueda
        if not valid_neighbors:
            break
        
        # Elegir el vecino con la menor altura
        next_i, next_j, next_height = min(valid_neighbors, key=lambda x: x[2])
        
        # Mover al vecino seleccionado
        trajectory.append((next_i, next_j))
        visited.add((next_i, next_j))
        current_height = next_height
        minimum_height = min([minimum_height, next_height])
        i, j = next_i, next_j
    
    # Convertir la trayectoria a coordenadas en metros
    trajectory_meters = [(j * scale, i * scale) for i, j in trajectory]
    
    return trajectory_meters, minimum_height

# Parámetros del mapa y posiciones iniciales
scale = 10.045  # Escala del mapa (metros por píxel)
start_positions = [
    (3350, 5800),  # Posición inicial
    (3000, 6000),  # Posición alterna inicial 1
    (4000, 5500),  # Posición alterna inicial 2
    (2000, 5000),  # Posición alterna inicial 3
    (5000, 7000),  # Posición alterna inicial 4
    (5500, 6000),  # Posición alterna inicial 5
]

# Ejecutar greedy desde cada posición inicial
results = []
index_starts = []
nr, nc = height_map.shape

def get_column(x):
    return round(x/scale)

def get_row(y):
    return nr - round(y/scale)

for x, y in start_positions:
    index_starts.append((get_row(y), get_column(x)))

for start_x, start_y in index_starts:
    trajectory, lowest_height = greedy_search(height_map, start_x, start_y, scale)
    results.append((start_x, start_y, trajectory, lowest_height))
    print(f"Posición inicial: ({start_x}, {start_y})")
    print(f"Punto más bajo alcanzado: {lowest_height} metros")
    print(f"Trayectoria: {len(trajectory)} pasos\n")


# Función para graficar la trayectoria
def plot_trajectory(height_map, trajectory, start_x, start_y, scale):
    plt.figure(figsize=(10, 8))
    plt.imshow(height_map, cmap='terrain', extent=[0, height_map.shape[1] * scale, 0, height_map.shape[0] * scale])
    plt.colorbar(label='Altura (m)')
    
    # Convertir la trayectoria a coordenadas en metros
    x_coords = [x for x, y in trajectory]
    y_coords = [y for x, y in trajectory]
    
    # Graficar la trayectoria
    plt.plot(x_coords, y_coords, 'r-', label='Trayectoria')
    plt.plot(start_x, start_y, 'bo', label='Inicio')
    plt.plot(x_coords[-1], y_coords[-1], 'go', label='Fin')
    
    plt.title(f"Trayectoria desde ({start_x}, {start_y})")
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.legend()
    plt.show()

# Graficar las trayectorias
for start_x, start_y, trajectory, _ in results:
    plot_trajectory(height_map, trajectory, start_x, start_y, scale)