import numpy as np
import matplotlib.pyplot as plt
import random
import math

height_map = np.load("mars_map.npy") 

def meters_to_indices(x, y, scale):
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

def simulated_annealing(height_map, start_x, start_y, scale, max_iter=1000, initial_temp=100.0, alpha=0.99, max_height_diff=2.0):
    """
    Realiza recocido simulado desde la posición inicial (start_x, start_y).
    Devuelve la trayectoria, la altura más baja alcanzada y la posición donde se alcanzó.
    """
    # Convertir coordenadas en metros a índices de la matriz
    i, j = meters_to_indices(start_x, start_y, scale)
    
    # Inicializar la trayectoria y la altura actual
    trajectory = [(i, j)]
    current_height = height_map[i, j]
    best_height = current_height
    best_position = (i, j)
    
    # Inicializar la temperatura
    T = initial_temp
    
    for iteration in range(max_iter):
        # Obtener vecinos válidos
        neighbors = get_neighbors(i, j)
        valid_neighbors = []
        for ni, nj in neighbors:
            if 0 <= ni < height_map.shape[0] and 0 <= nj < height_map.shape[1]:
                neighbor_height = height_map[ni, nj]
                if neighbor_height != -1 and abs(neighbor_height - current_height) <= max_height_diff:
                    valid_neighbors.append((ni, nj, neighbor_height))
        
        # Si no hay vecinos válidos, terminar la búsqueda
        if not valid_neighbors:
            break
        
        # Seleccionar un vecino aleatorio
        ni, nj, neighbor_height = random.choice(valid_neighbors)
        
        # Calcular la diferencia de altura
        delta_E = neighbor_height - current_height
        
        # Si el vecino es mejor, mover al explorador
        if delta_E < 0:
            i, j = ni, nj
            current_height = neighbor_height
            if current_height < best_height:
                best_height = current_height
                best_position = (i, j)
        # Si el vecino es peor, aplicar la regla de recocido simulado
        else:
            probability = math.exp(-delta_E / T)
            if random.random() < probability:
                i, j = ni, nj
                current_height = neighbor_height
        
        # Registrar la posición actual en la trayectoria
        trajectory.append((i, j))
        
        # Reducir la temperatura
        T *= alpha
    
    # Convertir la trayectoria a coordenadas en metros
    trajectory_meters = [(j * scale, i * scale) for i, j in trajectory]
    
    # Convertir best_position a coordenadas en metros
    best_position_meters = (best_position[1] * scale, best_position[0] * scale)
    
    return trajectory_meters, best_height, best_position_meters

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

# Ejecutar recocido simulado desde cada posición inicial
results = []
for start_x, start_y in start_positions:
    trajectory, lowest_height, best_position = simulated_annealing(height_map, start_x, start_y, scale)
    results.append((start_x, start_y, trajectory, lowest_height, best_position))
    print(f"Posición inicial: ({start_x}, {start_y})")
    print(f"Punto más bajo alcanzado: {lowest_height} metros")
    print(f"Posición del punto más bajo: {best_position}")
    print(f"Trayectoria: {len(trajectory)} pasos\n")

# Función para graficar la trayectoria
def plot_trajectory(height_map, trajectory, start_x, start_y, best_position, scale):
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
    
    # Marcar el punto más bajo
    plt.plot(best_position[0], best_position[1], 'mx', markersize=10, label='Punto más bajo')
    
    plt.title(f"Trayectoria desde ({start_x}, {start_y})")
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.legend()
    plt.show()

# Graficar las trayectorias
for start_x, start_y, trajectory, _, best_position in results:
    plot_trajectory(height_map, trajectory, start_x, start_y, best_position, scale)