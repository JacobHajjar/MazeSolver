#!/usr/bin/env python3
'''Solves a user drawn maze using AI'''
import pygame
from maze_drawer import MazeDrawer
pygame.init()

__author__ = 'Jacob Hajjar'
__email__ = 'hajjarj@csu.fullerton.edu'
__maintainer__ = 'jacobhajjar'

def main():
    '''the main function'''
    maze_drawer1 = MazeDrawer()
    maze_drawer1.start_drawing()


if __name__ == '__main__':
    main()
