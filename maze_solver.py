'''class file for the AI algorithm'''
import heapq
import constants


class MazeSolver():
    '''class that solves maze in a grid using A* algorithm'''

    def __init__(self,  grid, start_coordinate, goal_coordinate):
        self.grid = grid
        self.start_coordinate = start_coordinate
        self.goal_coordinate = goal_coordinate

    def solve_maze(self):
        '''returns true when maze is solved and false when maze is unsolvable'''
        frontier = [(0, self.start_coordinate)]
        explored = set(())
        while True:
            if not frontier:
                return False
            lowest_cost_cell = frontier[0]
            heapq.heappop(frontier)
            if lowest_cost_cell[1] == self.goal_coordinate:
                return True
            explored.add(lowest_cost_cell[1])
            self.grid[lowest_cost_cell[1][1]
                      ][lowest_cost_cell[1][0]] = constants.COM
            for child_cell in self.find_children(lowest_cost_cell):
                in_frontier = False
                in_explored = False
                for cell in frontier:
                    if child_cell == cell[1]:
                        in_frontier = True
                if child_cell in explored:
                    in_explored = True
                if not (in_frontier or in_explored):
                    frontier.append(
                        (self.generate_cost(child_cell), child_cell))
            heapq.heapify(frontier)

    def generate_cost(self, cell):
        '''return the cost of a cell movement by adding heuristic and distance'''
        return self.calculate_distance(cell) + self.calculate_heuristic(cell)

    def calculate_distance(self, cell):
        '''return the shortest distance in acceptable moves from start to the current cell'''
        return abs(cell[0] - self.start_coordinate[0]) + abs(cell[1] - self.start_coordinate[1])

    def calculate_heuristic(self, cell):
        '''return the heuristic based on the shortest distance directly from the current cell to the goal'''
        a_squared =  pow(cell[0] - self.goal_coordinate[0], 2)
        b_squared = pow(cell[1] - self.goal_coordinate[1], 2)
        return a_squared + b_squared

    def find_children(self, current_cell):
        '''returns a list of tuples for each child of the current cell'''
        max_height = len(self.grid)
        max_width = len(self.grid[0])
        child_list = []

        right_coordinate = current_cell[1][0] + 1
        right_cell = self.grid[current_cell[1][1]][right_coordinate]
        if (right_coordinate < max_width) and (right_cell != constants.MAZE):
            child_list.append((right_coordinate, current_cell[1][1]))

        left_coordinate = current_cell[1][0] - 1
        left_cell = self.grid[current_cell[1][1]][left_coordinate]
        if (left_coordinate >= 0) and (left_cell != constants.MAZE):
            child_list.append((left_coordinate, current_cell[1][1]))

        below_coordinate = current_cell[1][1] + 1
        below_cell =  self.grid[below_coordinate][current_cell[1][0]]
        if (below_coordinate < max_height) and (below_cell != constants.MAZE):
            child_list.append((current_cell[1][0], below_coordinate))

        above_coordinate = current_cell[1][1] - 1
        above_cell =  self.grid[above_coordinate][current_cell[1][0]]
        if (above_coordinate >= 0) and (above_cell != constants.MAZE):
            child_list.append((current_cell[1][0], above_coordinate))

        return child_list
