# Import libraries
import pygame
import os

from math import *

# Importing all custom made libraries
from CONST import *
from math import *

def draw_hexagon(surface, color, position, width=0):
    x, y = position
    pygame.draw.polygon(surface, color, [
        (x + HEXAGON_RADIUS * cos(2 * pi * i / HEXAGON_VERTICES), y + HEXAGON_RADIUS * sin(2 * pi * i / HEXAGON_VERTICES))  # Calculate the lines of the polygon
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
                draw_hexagon(surface, COLOR_DICT[col], (x, y))

def draw_pieces(surface, board):
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

def highlight_selected_hexagon(surface, position, board, selected_hexagon):
        amount_selected = 0
        board_pos = None
        for row in board:
            for elem in row:
                if elem.selected == True:
                    amount_selected += 1
                    board_pos = elem.pos
        try:
            y, x = POS_TO_TILE[position]
            if board[x][y].selected == False and amount_selected == 0 and board[x][y].piece != None:
                draw_hexagon(surface, COLOR_DICT['TARGET_COLOR'], position)
                board[x][y].selected = True
                return POS_TO_TILE[position]
            elif board[x][y].selected == True:
                draw_hexagon(surface, COLOR_DICT[ORIGINAL_COLORS[x][y]], position)
                board[x][y].selected = False
                return None
            if board_pos != (x,y):
                return selected_hexagon
        except:
            return selected_hexagon

