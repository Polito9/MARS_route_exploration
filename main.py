import numpy as np
from BFS import BFS
from InformedSearch import *
from time import perf_counter
from Graphics import plot_route

#Loading numpy array
mars_map = np.load('crater_map.npy')
nr, nc = mars_map.shape
scale = 10.045

#To convert the (x, y) coordinates into columns and rows
def get_column(x):
    return round(x/scale)

def get_row(y):
    return nr - round(y/scale)

#Initial point
x0 = 2850  
y0 = 6400  
row_0 = get_row(y0)
col_0 = get_column(x0)

#Target
xf = 3150 
yf = 6800 
row_f = get_row(yf)
col_f = get_column(xf)

'''
Algoritmos de busqueda usados: 
-BFS
-A*
-Greedy
-UCS (Dijkstra)
'''

#print(mars_map)

print("Origin: ", row_0, col_0)
print("Target: ", row_f, col_f)
MAX_HEIGHT_MOVEMENT = .3

#A*
print("WITH A*: ")
a_star = A_star(row_0, col_0, row_f, col_f, mars_map, MAX_HEIGHT_MOVEMENT)
time_0 = perf_counter()
steps = a_star.search()
print("Approximate distance traveled in meters: ", a_star.calculate_distance(steps, scale))
time_1 = perf_counter()
print(steps)
print("A* took: ", str(time_1-time_0))
plot_route(steps, mars_map, scale, "A*")


#Greedy
print("With Greedy Search")
greedy = GreedySearch(row_0, col_0, row_f, col_f, mars_map, MAX_HEIGHT_MOVEMENT)
time_0 = perf_counter()
steps = greedy.search()
print("Approximate distance traveled in meters: ", greedy.calculate_distance(steps, scale))
time_1 = perf_counter()
print(steps)
print("Greedy took: ", str(time_1-time_0))
plot_route(steps, mars_map, scale, "Greedy")
print()

#BFS
print("With BFS: ")
bf = BFS(row_0, col_0, row_f, col_f, mars_map, MAX_HEIGHT_MOVEMENT)
time_0 = perf_counter()
steps = bf.search()
print("Approximate distance traveled in meters: ", bf.calculate_distance(steps, scale))
print(steps)
time_1 = perf_counter()
print("BFS took: ", str(time_1-time_0))
plot_route(steps, mars_map, scale, "BFS")
print()


#UCS
print("With UCS: ")
ucs = UCS(row_0, col_0, row_f, col_f, mars_map, MAX_HEIGHT_MOVEMENT)
time_0 = perf_counter()
steps = ucs.search()
print("Approximate distance traveled in meters: ", ucs.calculate_distance(steps, scale))
time_1 = perf_counter()
print(steps)
print("UCS took: ", str(time_1-time_0))
plot_route(steps, mars_map, scale, "UCS")
print()

# Graficar los resultados (Quiero ver algunas cosas)
def plot_path(mars_map, path, title="Path"):
    plt.figure(figsize=(10, 10))
    plt.imshow(mars_map, cmap='hot', origin='upper')
    
    if path:
        rows, cols = zip(*[(p[0], p[1]) for p in path])
        plt.plot(cols, rows, marker="o", color="cyan", markersize=2, linewidth=1)

    plt.title(title)
    plt.colorbar()
    plt.show()
plot_path(mars_map, a_star.visited[row_f][col_f], "A* Path")
plot_path(mars_map, greedy.visited[row_f][col_f], "Greedy Path")
plot_path(mars_map, bf.visited[row_f][col_f], "BFS Path")
plot_path(mars_map, ucs.visited[row_f][col_f], "UCS Path")
