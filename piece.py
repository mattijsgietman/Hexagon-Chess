from CONST import *
from move import Move
from helper import on_board, empty_hexagon, piece_color_on_position, calculate_offset

class Piece:
    def __init__(self, color, position, coords):
        self.color = color
        self.position = position
        self.coords = coords
        self.moves = []


class Pawn(Piece):
    def __init__(self, color, position, coords):
        super().__init__(color, position, coords)
        self.name = 'pawn'
        self.dir = -1 if color == 'white' else 1
        self.has_moved = False

    def legal_moves(self, board):
        '''
        Calculate all the valid moves for a pawn to make
        '''

        self.moves = []
        position_col, position_row = self.position

        # Vertical moves  

        # Add going one step forward as a move
        target = (position_col, position_row + (2 * self.dir))
        if empty_hexagon(target, board):
            move = Move(self, self.position, target)
            self.moves.append(move)

            # Add going two steps forward as a move
            if not self.has_moved:
                target = (position_col, position_row + (4 * self.dir))
                if empty_hexagon(target, board):
                    move = Move(self, self.position, target)
                    self.moves.append(move)

        # Taking an enemy piece to the left
        target = (position_col, position_row + (1 * self.dir))
        if not empty_hexagon(target, board) and piece_color_on_position(target, board) != self.color:
            move = Move(self, self.position, target)
            self.moves.append(move)

        # Taking an enemy piece to the right
        target = (position_col + 1, position_row + (1 * self.dir))
        if not empty_hexagon(target, board) and piece_color_on_position(target, board) != self.color:
            move = Move(self, self.position, target)
            self.moves.append(move)

        return self.moves


class Knight(Piece):
    def __init__(self, color, position, coords):
        super().__init__(color, position, coords)
        self.name = 'knight'

    def legal_moves(self, board):
        '''
        Calculate all the valid moves for a knight to make
        '''
        
        self.moves = []
        position_col, position_row = self.position

        # Moving to the square 2 places up and 1 place to the left
        offset = calculate_offset(position_row, 1)
        target = (position_col - 1 - offset, position_row - 4)
        if on_board(target):
            if empty_hexagon(target, board) or piece_color_on_position(target, board) != self.color:
                move = Move(self, self.position, target)
                self.moves.append(move)


class Bishop(Piece):
    def __init__(self, color, position, coords):
        super().__init__(color, position, coords)
        self.name = 'bishop'

    def legal_moves(self, board):
        pass


class Rook(Piece):
    def __init__(self, color, position, coords):
        super().__init__(color, position, coords)
        self.name = 'rook'

    def legal_moves(self, board):
        pass


class Queen(Piece):
    def __init__(self, color, position, coords):
        super().__init__(color, position, coords)
        self.name = 'queen'

    def legal_moves(self, board):
        pass


class King(Piece):
    def __init__(self, color, position, coords):
        super().__init__(color, position, coords)
        self.name = 'king'
    

    def legal_moves(self, board):
        pass
