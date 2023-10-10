import math

from CONST import *
from draw import *

def find_closest_point(pos):
    '''
    Finds the closest hexagon based on a position
    '''
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
    '''
    Given a certain x,y position, check if there is a hexagon on screen
    '''
    try:
        return POS_TO_TILE[pos]         # Returns the index of the hexagon
    except:
        return None                     # Else returns None

def selected_hexagons(pos, selected_hexagon, board, turn, surface):
    '''
    Logic regarding what hexagon has to be selected, if this is the first or
    second hexagon which is selected, and when a square has to be deselected
    '''
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
    '''
    Deselect a hexagon after a move has been made, or the player clicked the hexagon again.
    '''
    draw_board(surface, COLOR_BOARD)
    draw_pieces(surface, board)
    return (None, None)

def deselect_piece(surface, board):
    '''
    Deselect a piece after a move has been made, or the piece has been pressed again
    '''
    draw_board(surface, COLOR_BOARD)
    draw_pieces(surface, board)
    return None

def switch_turns(turn):
    '''
    Switch the turn between players
    '''
    if turn == 'white':
        return 'black'
    return 'white'

def make_move(board, move, piece):
    '''
    When a move is made, make the actual move on the board
    '''
    board[move.initial[1]][move.initial[0]].piece = None
    piece.position = move.target
    piece.coords = TILE_TO_POS[piece.position]
    board[move.target[1]][move.target[0]].piece = piece

def on_board(position, board):
    '''
    Check if a given position is on the board
    '''
    row, col = position
    try:
        if board[col][row] != None:
            return True
    except:
        return False

def empty_hexagon(position, board):
    '''
    Return if a square is empty
    '''
    row, col = position
    try:
        if board[col][row].piece == None:
            return True
    except:
        return False

def piece_color_on_position(position, board):
    '''
    Return if a square is empty
    '''
    row, col = position
    return board[col][row].piece.color

def find_target_locations(moves):
    '''
    Gatheres all the locations where a piece can go to, such that we can draw this on the screen
    '''
    targets = []
    for move in moves:
        targets.append(move.target)
    return targets

def has_moved(piece):
    '''
    Sets the variable has_moved true for a pawn if it moves
    '''
    if piece.name == 'pawn':
        piece.has_moved = True
