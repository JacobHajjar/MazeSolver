'''class file for the AI algorithm'''
import heapq
import math
import constants
class MazeSolver():
    '''class that solves maze in a grid using A* algorithm'''

    def __init__(self,  grid):
        self.grid = grid

    def solve_maze(self, start_coordinate, goal_coordinate):
        '''returns true when maze is solved and false when maze is unsolvable'''
        frontier = [(0, start_coordinate)]
        explored = set(())
        while True:
            if not frontier:
                return False
            lowest_cost_cell = frontier[0]
            heapq.heappop(frontier)
            if lowest_cost_cell is goal_coordinate:
                return True
            explored.add((0, lowest_cost_cell))
            for child_cell in self.find_children(lowest_cost_cell):
                in_frontier = False
                in_explored = False
                found_index = 0
                for index, cell in enumerate(frontier):
                    if child_cell[1] == cell[1]:
                        in_frontier = True
                        found_index = index
                for index, cell in enumerate(explored):
                    if child_cell[1] == cell[1]:
                        in_explored = True
                if not in_frontier and in_explored:
                    frontier.append((self.generate_cost(child_cell, start_coordinate, goal_coordinate), child_cell))
                #elif in_frontier:
                #        if frontier[found_index]

                 
    
    def generate_cost(self, cell, start_coordinate, goal_coordinate):
        '''return the cost of a cell movement by adding heuristic and distance'''
        return self.calculate_distance(cell, start_coordinate) + self.calculate_heuristic(cell, goal_coordinate)

    def calculate_distance(self, cell, start_coordinate):
        '''return the shortest distance in acceptable moves from start to the current cell'''
        return abs(cell[0] - start_coordinate[0]) + abs(cell[1] - start_coordinate[1])
        
        
    def calculate_heuristic(self, cell, goal_coordinate):
        '''return the heuristic based on the shortest distance directly from the current cell to the goal'''
        return pow(cell[0] - goal_coordinate[0], 2) + pow(cell[1] - goal_coordinate[1], 2)

    def find_children(self, current_cell):
        '''returns a list of tuples for each child of the current cell'''
        max_height = len(self.grid) - 1
        max_width = len(self.grid[0]) - 1
        child_list = []
        if current_cell[1][0] + 1 < max_width:
            child_list.append((current_cell[1][0] + 1, current_cell[1][1]))
        if current_cell[1][0] - 1 >= 0:
            child_list.append((current_cell[1][0] - 1, current_cell[1][1]))
        if current_cell[1][1] + 1 < max_height:
            child_list.append((current_cell[1][0], current_cell[1][1] + 1))
        if current_cell[1][1] - 1 >= 0:
            child_list.append((current_cell[1][0], current_cell[1][1] - 1))
        return child_list       
       