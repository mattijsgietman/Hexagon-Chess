# Import libraries
import pygame
from math import *

# Importing all custom made libraries
from CONST import *
from math import *

def draw_hexagon(surface, color, position, width=0):
    x, y = position
    pygame.draw.polygon(surface, color, [
        (x + HEXAGON_RADIUS * cos(2 * pi * i / HEXAGON_VERTICES), y + HEXAGON_RADIUS * sin(2 * pi * i / HEXAGON_VERTICES))
        for i in range(HEXAGON_VERTICES)
    ], width)

def draw_board(surface, color_board):
    for i, row in enumerate(color_board):
        for j, col in enumerate(row):
            # Calculate the position of each hexagon in the grid
            x = TOP_SQ_X + j * SPACING_X
            y = TOP_SQ_Y + i * SPACING_Y

            # Alternate the rows horizontally to create the honeycomb pattern
            if i % 2 != 0:
                x += SPACING_X / 2
            if(col != '-'):
                print(i, j)
                draw_hexagon(surface, COLOR_DICT[col], (x, y))
