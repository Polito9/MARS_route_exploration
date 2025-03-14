import numpy as np
from BFS import BFS
from InformedSearch import *
from time import perf_counter
import matplotlib.pyplot as plt #Para ver los resultados

#Loading numpy array
mars_map = np.load('crater_map.npy')
nr, nc = mars_map.shape
scale = 10.045

#To convert the (x, y) coordinates into columns and rows
def get_column(x):
    return round(x/scale)

def get_row(y):
    return nr - round(y/scale)

#Initial points
#X0 = 2300
#Y0 = 4000

#x0 = 3000
#y0 = 6000

x0 = 3200
y0 = 5000
row_0 = get_row(y0)
col_0 = get_column(x0)

#Target
xf = 3350 
yf = 5800
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
MAX_HEIGHT_MOVEMENT = .1991

#A*
print("WITH A*: ")
a_star = A_star(row_0, col_0, row_f, col_f, mars_map, MAX_HEIGHT_MOVEMENT)
time_0 = perf_counter()
a_star.search()
time_1 = perf_counter()
print("A* took: ", str(time_1-time_0))
print()

#Greedy
print("With Greedy Search")
greedy = GreedySearch(row_0, col_0, row_f, col_f, mars_map, MAX_HEIGHT_MOVEMENT)
time_0 = perf_counter()
greedy.search()
time_1 = perf_counter()

print("Greedy took: ", str(time_1-time_0))
print()

#BFS
print("With BFS: ")
bf = BFS(row_0, col_0, row_f, col_f, mars_map, MAX_HEIGHT_MOVEMENT)
time_0 = perf_counter()
bf.search()
time_1 = perf_counter()
print("BFS took: ", str(time_1-time_0))
print()

#UCS
print("With UCS: ")
ucs = UCS(row_0, col_0, row_f, col_f, mars_map, MAX_HEIGHT_MOVEMENT)
time_0 = perf_counter()
ucs.search()
time_1 = perf_counter()
print("UCS took: ", str(time_1-time_0))
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
