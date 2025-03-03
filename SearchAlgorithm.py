class SearchAlgorithm:
    row_0 = 0
    col_0 = 0
    row_f = 0
    col_f = 0
    mars_map = []
    visited = [] #If a value there is -2, the cell is visited
    #visited = set() #The visited set will save in string the column and row
    def __init__(self, row_0, col_0, row_f, col_f, mars_map):
        self.row_0 = row_0
        self.row_f = row_f
        self.col_f = col_f
        self.col_0 = col_0
        self.mars_map = mars_map
        
        #creating an empty 2D array of visited
        for _ in range(len(mars_map)):
            sub_array = []
            for _ in range(len(mars_map[0])):
                sub_array.append(False)
            
            self.visited.append(sub_array)

    def validate_state(self, row_a0, col_a0,row_a1, col_a1):
        #Validate that it is not -1 and the difference is less than .25
        if(self.mars_map[row_a1][col_a1] == -1):
            return False
        
        n1 = self.mars_map[row_a1][col_a1]
        n2 = self.mars_map[row_a0][col_a0]
        dif = abs(n1 - n1)
        
        if(dif>=.25):
            return False
        
        return True
     
    def calculate_heuristic(self, row_a, col_a):
        #Calculates the distance between two points, and this is the heuristic
        return ((row_a - self.row_f)**2 + (col_a - self.col_f)**2)**(1/2)

    def calculate_next_steps(self, row_a, col_a):
        #Goes through all the possible states and validates that it is possible to be there
        aux = [-1, 0, 1]
        steps = []
        for i in aux:
            for j in aux:
                if((not self.visited[row_a+i][col_a+j]) and self.validate_state(row_a, col_a, row_a+i, col_a+j)):
                    #print("In: ", len(self.visited))
                    steps.append((row_a+i, col_a+j))
        return steps
        