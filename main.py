import numpy as np

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
row_f = get_row(xf)
col_f = get_column(yf)

'''
Algoritmos de busqueda usados: 
-BFS
-A*
-Greedy
-UCS (Dijkstra)
'''