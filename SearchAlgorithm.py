from collections import deque

class SearchAlgorithm:
    row_0 = 0
    col_0 = 0
    row_f = 0
    col_f = 0
    mars_map = []

    def __init__(self, row_0, col_0, row_f, col_f, mars_map):
        self.row_0 = row_0
        self.row_f = row_f
        self.col_f = col_f
        self.col_0 = col_0
        self.mars_map = mars_map
    
    def validate_state(self, row_a0, col_a0,row_a1, col_a1):
        if(self.mars_map[row_a1][col_a1] == -1):
            return False
        dif = abs(self.mars_map[row_a1][col_a1] - self.mars_map[row_a0][col_a0])
        
        if(dif>=.25):
            return False
        return True
     
    def calculate_heuristic(self, row_a, col_a):
        #Calculates the distance between two points, and this is the heuristic
        return ((row_a - self.row_f)**2 + (col_a - self.col_f)**2)**(1/2)
    
    def bfs(self):
        #The algorithm will save in the queue tuples of size two representing the row and column to save
        #The visited set will save in string the column and row
        '''
        -1 0
        -1 -1
        0 -1
        1 0
        0 1
        1 1
        1 -1
        -1 1
        '''
        deque.append()