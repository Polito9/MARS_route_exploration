from SearchAlgorithm import SearchAlgorithm
from queue import PriorityQueue

class InformedSearch(SearchAlgorithm):
    def __init__(self, row_0, col_0, row_f, col_f, mars_map, max_height_movement):
        super().__init__(row_0, col_0, row_f, col_f, mars_map, max_height_movement)

    def search(self):
        founded = False

        #The starting point
        queue = PriorityQueue()
        queue.put((self.get_cost(self.row_0, self.col_0, self.row_0, self.col_0) , (self.row_0, self.col_0, [(self.row_0, self.col_0)])))        
        #Doing the Greedy Search
        while(not queue.empty()):
            if(founded):
                break
            actual = queue.get()
            actual = actual[1]
            if(len(self.visited[actual[0]][actual[1]])>0):
                continue

            self.visited[actual[0]][actual[1]] = actual[2]

            #print(len(self.visited))
            #print("Actual: ",actual)
            if(actual[0] == self.row_f  and actual[1] == self.col_f):
                #print("Founded in ", actual[2])
                #print("It took ", len(actual[2]), " steps")
                founded = True
                return actual[2]
            
            steps = self.calculate_next_steps(actual[0], actual[1], actual[2])
            #print("That steps: ", steps)
            for s in steps:
                queue.put((self.get_cost(actual[0], actual[1], s[0], s[1]) , s))
        
        if(not founded):
            print("The algorithm does not found the target")

        return []
    def get_cost(self, row_a0, col_a0, row_a1, col_a1):
        #When using only heuristic, the only aspect that matters is the first two arguments
        pass


class GreedySearch(InformedSearch):
    def get_cost(self, row_a0, col_a0, row_a1, col_a1):
        return self.calculate_heuristic(row_a0, col_a0)

class A_star(InformedSearch):
    def get_cost(self, row_a0, col_a0, row_a1, col_a1):
        return self.calculate_heuristic(self.row_0, self.col_0) + self.calculate_cost(row_a0 ,col_a0 ,row_a1, col_a1)
    
class UCS(InformedSearch):
    def get_cost(self, row_a0, col_a0, row_a1, col_a1):
        return self.calculate_cost(row_a0 ,col_a0 ,row_a1, col_a1)