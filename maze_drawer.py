'''class containing the maze drawing functionality'''
from collections import namedtuple
import sys
import math
import pygame
from pygame.locals import *
pygame.init()

BLANK = 0
MAZE = 1
COM = 2
START = 3
GOAL = 4

Colors = namedtuple(
    'Colors', ['black', 'lgray', 'white', 'red', 'yellow', 'blue', 'lime', 'aqua', 'purple'])


class MazeDrawer:
    '''class that will draw the maze'''
    colors = Colors((0, 0, 0), (100, 100, 100), (255, 255, 255), (255,   0,   0), (255, 255,   0),
                    (0,  0, 255), (0, 255,   0), (0, 255, 255), (128,  0, 128))

    curr_mouse = [-1, -1]
    grid = []
    window_width = 800
    window_height = 700
    display_surf = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Maze Solver")

    def start_drawing(self):
        '''start the drawing of the maze'''
        self.generate_grid(20)  # generate the grid 20 x 15
        fps_clock = pygame.time.Clock()
        while True:  # game started loop
            self.curr_mouse = [-1, -1]
            for event in pygame.event.get():  # event handling loop
                #pylint: disable=E0602
                # ^ pylint doesn't like pygame event variables :(
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    mousex, mousey = event.pos
                    self.curr_mouse = [mousex, mousey]
            self.display_scene()
            pygame.display.update()
            fps_clock.tick(15)

    def display_scene(self):
        '''the logic and objects displayed in the scene'''
        self.display_surf.fill(self.colors.lgray)
        margin = 20
        box_size = (self.window_width - (margin * 2)) / len(self.grid[0])
        self.check_clicks_to_grid(box_size, margin)
        # start button
        start_rect = pygame.Rect(margin, (margin * 2) + (box_size * len(self.grid)),
                                 ((box_size * len(self.grid[0])) / 2) - margin, box_size * 1.5)
        pygame.draw.rect(self.display_surf, self.colors.lime, start_rect, 0)
        pygame.draw.rect(self.display_surf, self.colors.black, start_rect, 2)
        # clear button
        clear_rect = pygame.Rect(margin, (margin * 2) + (box_size * len(self.grid)),
                                 ((box_size * len(self.grid[0])) / 2) - margin, box_size * 1.5)
        pygame.draw.rect(self.display_surf, self.colors.yellow, clear_rect, 0)
        pygame.draw.rect(self.display_surf, self.colors.black, clear_rect, 2)

        self.draw_grid(box_size, margin)

    def generate_grid(self, dims):
        '''generate the maze grid'''
        self.grid = [[BLANK for _ in range(dims)]
                     for _ in range(math.floor(dims * 0.75))]
        self.grid[7][0] = START
        self.grid[7][19] = GOAL

    def draw_grid(self, box_size, margin):
        '''draw the maze grid'''
        # colors for BLANK, MAZE, COM, START, GOAL
        grid_colors = [self.colors.white, self.colors.black,
                       self.colors.purple, self.colors.blue, self.colors.red]
        for row_index, row in enumerate(self.grid):
            for col_index, cell in enumerate(row):
                grid_box = pygame.Rect(
                    margin + (col_index * box_size), margin +
                    (row_index * box_size),
                    box_size, box_size)
                pygame.draw.rect(self.display_surf,
                                 grid_colors[cell], grid_box, 0)
                pygame.draw.rect(self.display_surf,
                                 self.colors.black, grid_box, 1)

    def check_clicks_to_grid(self, box_size, margin):
        '''checks if a click was made inside the grid'''
        col = math.floor((self.curr_mouse[0] - margin) / box_size)
        row = math.floor((self.curr_mouse[1] - margin) / box_size)
        if (len(self.grid) > row >= 0 and len(self.grid[0]) > col >= 0):
            if self.grid[row][col] not in [3, 4]:
                self.grid[row][col] = MAZE

    def add_maze(self):
        '''get the grid index from grid coordinate'''
