#!/usr/bin/env python3
'''a maze solving AI using theh A* algorithm'''
import pygame
from maze_drawer import MazeDrawer
pygame.init()

__author__ = 'Jacob Hajjar'
__email__ = 'hajjarj@csu.fullerton.edu'
__maintainer__ = 'jacobhajjar'


class MazeSolver:
    '''class that will solve the drawn maze'''


def main():
    '''the main function'''
    maze_drawer1 = MazeDrawer()
    maze_drawer1.start_drawing()


if __name__ == '__main__':
    main()
