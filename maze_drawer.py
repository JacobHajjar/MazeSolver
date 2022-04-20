'''class containing the maze drawing functionality'''
from enum import IntEnum
from collections import namedtuple
import sys
import math
from turtle import clear
import pygame
from pygame.locals import *
from maze_solver import MazeSolver
pygame.init()




Colors = namedtuple(
    'Colors', ['black', 'lgray', 'white', 'red', 'yellow', 'blue', 'lime', 'aqua', 'purple'])

class Types(IntEnum):
    '''class of all the grid types'''
    BLANK = 0
    MAZE = 1
    COM = 2
    START = 3
    GOAL = 4

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
        button_top_margin = (margin * 2) + (box_size * len(self.grid))
        button_width = (box_size * len(self.grid[0]) / 2) - margin
        button_height = box_size * 1.5
        self.check_clicks_to_grid(box_size, margin)

        # start button
        start_clicked = self.draw_clickable_button(margin, button_top_margin, button_width,
                                   button_height, self.colors.lime, "SOLVE MAZE")

        # clear button
        clear_clicked = self.draw_clickable_button(self.window_width - (button_width + margin),
                                   button_top_margin, button_width,
                                   button_height, self.colors.yellow, "CLEAR GRID")
        if start_clicked:
            print("start clicked")
            maze_solver1 = MazeSolver(Types)
            maze_solver1.printTest()
        elif clear_clicked:
            print("clear clicked")
        self.draw_grid(box_size, margin)

    def generate_grid(self, dims):
        '''generate the maze grid'''
        self.grid = [[Types.BLANK for _ in range(dims)]
                     for _ in range(math.floor(dims * 0.75))]
        self.grid[7][0] = Types.START
        self.grid[7][19] = Types.GOAL

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
                self.grid[row][col] = Types.MAZE

    def generate_maze_1(self):
        '''generate the first default maze'''

    def draw_clickable_button(self, left, top, width, height, color, text):
        '''draw a clickable button in the scene that returns true if clicked'''
        outline_size = 2
        button_font_size = 35
        mousex, mousey = pygame.mouse.get_pos()
        button_rect = pygame.Rect(left, top, width, height)
        drawn_button = pygame.draw.rect(
            self.display_surf, color, button_rect, 0)
        pygame.draw.rect(self.display_surf, self.colors.black, button_rect, 2)
        if drawn_button.collidepoint(mousex, mousey):
            outline_size = 4
        pygame.draw.rect(self.display_surf, self.colors.black,
                         button_rect, outline_size)
        text_rend, text_box = load_default_text(
            button_font_size, self.colors.black, text)
        text_box.center = button_rect.center
        self.display_surf.blit(text_rend, text_box)
        if drawn_button.collidepoint(self.curr_mouse[0], self.curr_mouse[1]):
            return True
        return False


def load_default_text(size, col, msg):
    '''function to help load text'''
    font_obj = pygame.font.SysFont('Ariel', size)
    font_render = font_obj.render(msg, True, col, None)
    return font_render, font_render.get_rect()
