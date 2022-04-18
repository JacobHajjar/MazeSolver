'''class containing the maze drawing functionality'''
from collections import namedtuple
from ctypes import sizeof
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
    window_height = 640
    display_surf = pygame.display.set_mode((window_width, window_height))

    def _init_(self):
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
        self.display_surf.fill(self.colors.white)

    def generate_grid(self, dims):
        '''generate the maze grid'''
        self.grid = [[BLANK for _ in range(dims)]
                     for _ in range(math.floor(dims * 0.75))]
        self.grid[7][0] = START
        self.grid[7][19] = GOAL

    def draw_grid(self):
        '''draw the maze grid'''
        margin = 20
        box_size = (self.window_width - (margin * 2)) / sizeof(self.grid[0])

    def convert_to_grid(self):
        '''convert pixel coordinate to grid coordinate'''

    def get_grid_index(self):
        '''get the grid index from grid coordinate'''
