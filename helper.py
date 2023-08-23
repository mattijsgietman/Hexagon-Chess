import math

from CONST import *
from draw import *

def find_closest_point(pos):
    min_distance = float('inf')
    closest_point = None

    for point in ALL_POS:   # Loop over all points on the screen
        x1, y1 = point
        x2, y2 = pos
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)   # Find distance between clicked point and target point
        if distance < min_distance:
            min_distance = distance
            closest_point = point

    if closest_point in HEXAGON_POS:    # Check if closest point is on a hexagon
        return closest_point            # Return closest point if it is a hexagon
    else:
        return None                     # Else return None

def find_hexagon(pos):
    try:
        return POS_TO_TILE[pos]         # Returns the index of the hexagon
    except:
        return None                     # Else returns None

def selected_hexagons(pos, selected_hexagon, board, turn, surface):
    first, second = selected_hexagon
    hexagon = find_hexagon(pos)
    y,x = hexagon
    try:
        selected_color = board[x][y].piece.color
    except:
        selected_color = None

    if first is None and second is None and selected_color == turn:
        board[x][y].selected = True
        return (hexagon, None)
    elif first is not None and second is None and hexagon is not first and selected_color != turn:
        board[x][y].selected = True
        return (first, hexagon)
    elif first is not None and second is None and hexagon is not first and selected_color == turn:
        return (first, None)
    elif first is not None and second is not None and first != second:
        board[x][y].selected = True
        return (first, second)
    elif first is not None and first == hexagon:
        draw_board(surface, COLOR_BOARD)
        draw_pieces(surface, board)
        return (None, None) 
    else:
        return (None, None)

def deselect_hexagons(surface, board):
    draw_board(surface, COLOR_BOARD)
    draw_pieces(surface, board)
    return (None, None)

def switch_turns(turn):
    if turn == 'white':
        return 'black'
    return 'white'


def make_move(board, move, piece):
    board[move.initial[1]][move.initial[0]].piece = None
    piece.position = move.target
    piece.coords = TILE_TO_POS[piece.position]
    board[move.target[1]][move.target[0]].piece = piece

