from SearchAlgorithm import SearchAlgorithm
from collections import deque

class BFS(SearchAlgorithm):
    
    def __init__(self, row_0, col_0, row_f, col_f, mars_map):
        super().__init__(row_0, col_0, row_f, col_f, mars_map)


    def search(self):
        #print(self.row_f, self.col_f)
        #The algorithm will save in the queue tuples of size two representing the row and column to save
        founded = False

        #The starting point
        queue = deque()
        queue.append((self.row_0, self.col_0, [(self.row_0, self.col_0)]))        
        #Doing the bfs
        while(len(queue)>0 and not founded):
            actual = queue.popleft()
            if(len(self.visited[actual[0]][actual[1]])>0):
                continue

            self.visited[actual[0]][actual[1]] = actual[2]

            #print(len(self.visited))
            #print("Actual: ",actual)
            if(actual[0] == self.row_f  and actual[1] == self.col_f):
                print("Founded in ", actual[2])
                print("It took ", len(actual[2]), " steps")
                founded = True

            steps = self.calculate_next_steps(actual[0], actual[1], actual[2])
            #print("That steps: ", steps)
            for s in steps:
                queue.append(s)
        
        if(not founded):
            print("The algorithm does not found the target")