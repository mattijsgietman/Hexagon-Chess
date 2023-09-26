# Import libraries
import pygame
import os

from math import *

# Importing all custom made libraries
from CONST import *
from math import *

def draw_hexagon(surface, color, position, width=0):
    '''
    Function to draw a single hexagon
    '''
    x, y = position
    pygame.draw.polygon(surface, color, [
        (x + HEXAGON_RADIUS * cos(2 * pi * i / HEXAGON_VERTICES), y + HEXAGON_RADIUS * sin(2 * pi * i / HEXAGON_VERTICES))  # Calculate the lines of the polygon
        for i in range(HEXAGON_VERTICES)
    ], width)

def draw_board(surface, color_board):
    '''
    Function to draw all the hexagons that make up the chess board
    '''
    for i, row in enumerate(color_board):
        for j, col in enumerate(row):
            # Calculate the position of each hexagon in the grid
            x = TOP_SQ_X + j * SPACING_X
            y = TOP_SQ_Y + i * SPACING_Y

            # Alternate the rows horizontally to create the honeycomb pattern
            if i % 2 != 0:
                x += SPACING_X / 2
            if(col != '-'):
                draw_hexagon(surface, COLOR_DICT[col], (x, y))

def draw_pieces(surface, board):
    '''
    Function that draws all the pieces on the chessboard
    '''
    for row in board:
        for col in row:
            if col.piece != None:
                color = col.piece.color
                name = col.piece.name
                x, y = col.piece.coords
                texture = os.path.join(f'images/imgs-80px/{color}_{name}.png')
                img = pygame.image.load(texture)
                img = pygame.transform.scale(img, (50,50))
                surface.blit(img, (x-25, y-25))

def draw_selected_hexagons(surface, positions):
    '''
    Function to visualize which hexagon(s) has been selected. This function is also used to visualize the legal moves of a piece
    '''
    for pos in positions:
        if pos != None:
            x, y = pos
            coord = TILE_TO_POS[pos]
            draw_hexagon(surface, COLOR_DICT['TARGET_COLOR'], coord) 

