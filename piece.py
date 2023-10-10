from CONST import *
from move import Move
from helper import on_board, empty_hexagon, piece_color_on_position

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
        self.has_moved = False

    def legal_moves(self, board):
        '''
        Calculate all the valid moves for a pawn to make
        '''

        self.moves = []
        position_col, position_row = self.position

        target = (position_col, position_row - 2) if self.color == 'white' else (position_col, position_row + 2)
        if on_board(target, board) and empty_hexagon(target, board):
            move = Move(self, self.position, target)
            self.moves.append(move)
        
        if on_board(target, board) and empty_hexagon(target, board) and self.has_moved == False:
            target = (position_col, position_row - 4) if self.color == 'white' else (position_col, position_row + 4)
            if on_board(target, board) and empty_hexagon(target, board):
                move = Move(self, self.position, target)
                self.moves.append(move)

        target = (position_col - 1, position_row - 1) if self.color == 'white' else (position_col - 1, position_row + 1)
        if on_board(target, board) and not empty_hexagon(target, board) and piece_color_on_position(target, board) != self.color:
            move = Move(self, self.position, target)
            self.moves.append(move)
        
        target = (position_col + 1, position_row - 1) if self.color == 'white' else (position_col + 1, position_row + 1)
        if on_board(target, board) and not empty_hexagon(target, board) and piece_color_on_position(target, board) != self.color:
            move = Move(self, self.position, target)
            self.moves.append(move)


class Knight(Piece):
    def __init__(self, color, position, coords):
        super().__init__(color, position, coords)
        self.name = 'knight'

    def legal_moves(self, board):
        '''
        Calculate all the valid moves for a knight to make
        '''
        self.moves = []
        directions = [
            (-1, -5), (-2, -4), (1, -5), (2, -4),
            (3, -1), (3, 1), (-3, 1), (-3, -1),
            (-1, 5), (-2, 4), (1, 5), (2, 4)
            ]
        position_col, position_row = self.position

        for direction in directions:
            direction_col, direction_row = direction
            target = (position_col + direction_col, position_row + direction_row)
            if on_board(target, board):
                if empty_hexagon(target, board) or piece_color_on_position(target, board) != self.color:
                    move = Move(self, self.position, target)
                    self.moves.append(move)

class Bishop(Piece):
    def __init__(self, color, position, coords):
        super().__init__(color, position, coords)
        self.name = 'bishop'

    def legal_moves(self, board):
        self.moves = []
        directions = [(-1, -3), (1, -3), (-1, 3), (1,3), (2,0), (-2,0)]

        for direction in directions:
            counter = 1
            position_col, position_row = self.position
            direction_col, direction_row = direction
            target = (position_col + direction_col, position_row + direction_row)

            while True:
                target = (position_col + (direction_col * counter), position_row + (direction_row * counter))
                if on_board(target, board):
                    if not empty_hexagon(target, board) and piece_color_on_position(target, board) == self.color:
                        break
                    if not empty_hexagon(target, board) and piece_color_on_position(target, board) != self.color:
                        move = Move(self, self.position, target)
                        self.moves.append(move)
                        break
                    move = Move(self, self.position, target)
                    self.moves.append(move)
                    counter += 1
                else:
                    break

class Rook(Piece):
    def __init__(self, color, position, coords):
        super().__init__(color, position, coords)
        self.name = 'rook'

    def legal_moves(self, board):
        self.moves = []
        directions = [(0, -2), (1, -1), (1, 1), (0, 2), (-1, 1), (-1, -1)]

        for direction in directions:
            counter = 1
            position_col, position_row = self.position
            direction_col, direction_row = direction
            target = (position_col + direction_col, position_row + direction_row)

            while True:
                target = (position_col + (direction_col * counter), position_row + (direction_row * counter))
                if on_board(target, board):
                    if not empty_hexagon(target, board) and piece_color_on_position(target, board) == self.color:
                        break
                    if not empty_hexagon(target, board) and piece_color_on_position(target, board) != self.color:
                        move = Move(self, self.position, target)
                        self.moves.append(move)
                        break
                    move = Move(self, self.position, target)
                    self.moves.append(move)
                    counter += 1
                else:
                    break


class Queen(Piece):
    def __init__(self, color, position, coords):
        super().__init__(color, position, coords)
        self.name = 'queen'

    def legal_moves(self, board):
        self.moves = []
        directions = [(-1, -3), (1, -3), (-1, 3), (1,3), (2,0), (-2,0), (0, -2), (1, -1), (1, 1), (0, 2), (-1, 1), (-1, -1)]

        for direction in directions:
            counter = 1
            position_col, position_row = self.position
            direction_col, direction_row = direction
            target = (position_col + direction_col, position_row + direction_row)

            while True:
                target = (position_col + (direction_col * counter), position_row + (direction_row * counter))
                if on_board(target, board):
                    if not empty_hexagon(target, board) and piece_color_on_position(target, board) == self.color:
                        break
                    if not empty_hexagon(target, board) and piece_color_on_position(target, board) != self.color:
                        move = Move(self, self.position, target)
                        self.moves.append(move)
                        break
                    move = Move(self, self.position, target)
                    self.moves.append(move)
                    counter += 1
                else:
                    break


class King(Piece):
    def __init__(self, color, position, coords):
        super().__init__(color, position, coords)
        self.name = 'king'
    

    def legal_moves(self, board):
        self.moves = []
        directions = [(0,-2), (-1,-3), (1, -3), (-1,-1), (1, -1),
                      (-2, 0), (2, 0),
                      (-1,-1), (1,1), (0,2), (-1, 1), (-1, 3), (1,3)  
                     ]
        position_col, position_row = self.position

        for direction in directions:
            direction_col, direction_row = direction
            target = (position_col + direction_col, position_row + direction_row)
            if on_board(target, board):
                if empty_hexagon(target, board) or piece_color_on_position(target, board) != self.color:
                    move = Move(self, self.position, target)
                    self.moves.append(move)
