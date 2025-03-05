import numpy as np
from BFS import BFS
from InformedSearch import *

#Loading numpy array
mars_map = np.load('mars_map.npy')
nr, nc = mars_map.shape
scale = 10.0174

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
MAX_HEIGHT_MOVEMENT = .25

#Greedy
print("With Greedy Search")
greedy = GreedySearch(row_0, col_0, row_f, col_f, mars_map, MAX_HEIGHT_MOVEMENT)
greedy.search()

#BFS
print("With BFS: ")
bf = BFS(row_0, col_0, row_f, col_f, mars_map, MAX_HEIGHT_MOVEMENT)
bf.search()

#UCS
print("With UCS: ")
ucs = UCS(row_0, col_0, row_f, col_f, mars_map, MAX_HEIGHT_MOVEMENT)
ucs.search()

#A*
print("WITH A*: ")
a_star = A_star(row_0, col_0, row_f, col_f, mars_map, MAX_HEIGHT_MOVEMENT)
a_star.search()