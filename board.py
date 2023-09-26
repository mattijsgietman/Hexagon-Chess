from hexagon import *
from CONST import *
from piece import *

class Board():
    def __init__(self):
        self.board =  [
            [None],
            [None, None],
            [None, None, None],
            [None, None, None, None],
            [None, None, None, None, None],
            [None, None, None, None, None, None],
            [None, None, None, None, None, None],
            [None, None, None, None, None, None],
            [None, None, None, None, None],
            [None, None, None, None, None, None],
            [None, None, None, None, None],
            [None, None, None, None, None, None],
            [None, None, None, None, None],
            [None, None, None, None, None, None],
            [None, None, None, None, None, None],
            [None, None, None, None, None, None],
            [None, None, None, None, None],
            [None, None, None, None],
            [None, None, None,],
            [None, None],
            [None]
        ]
    
    def hexagon_setup(self):
        for key in TILE_TO_POS:
            y, x = key
            hex = Hexagon(key)
            hex.coords = TILE_TO_POS[key]
            self.board[x][y] = hex

    def piece_setup(self):
        # Setting up the black pieces
        self.board[0][0].piece = Bishop('black', (0,0), TILE_TO_POS[(0,0)])
        self.board[1][0].piece = Queen('black', (0,1), TILE_TO_POS[(0,1)])
        self.board[1][1].piece = King('black', (1,1), TILE_TO_POS[(1,1)])
        self.board[2][0].piece = Knight('black', (0,2), TILE_TO_POS[(0,2)])
        self.board[2][1].piece = Bishop('black', (1,2), TILE_TO_POS[(1,2)])
        self.board[2][2].piece = Knight('black', (2,2), TILE_TO_POS[(2,2)])
        self.board[3][0].piece = Rook('black', (0,3), TILE_TO_POS[(0,3)])
        self.board[3][3].piece = Rook('black', (3,3), TILE_TO_POS[(3,3)])
        self.board[4][0].piece = Pawn('black', (0,4), TILE_TO_POS[(0,4)])
        self.board[4][2].piece = Bishop('black', (2,4), TILE_TO_POS[(2,4)])
        self.board[4][4].piece = Pawn('black', (4,4), TILE_TO_POS[(4,4)])
        self.board[5][1].piece = Pawn('black', (1,5), TILE_TO_POS[(1,5)])
        self.board[5][4].piece = Pawn('black', (4,5), TILE_TO_POS[(4,5)])
        self.board[6][5].piece = Pawn('black', (5,6), TILE_TO_POS[(5,6)])  # testing
        self.board[6][1].piece = Pawn('black', (1,6), TILE_TO_POS[(1,6)])
        self.board[6][3].piece = Pawn('black', (3,6), TILE_TO_POS[(3,6)])
        self.board[7][2].piece = Pawn('black', (2,7), TILE_TO_POS[(2,7)])
        self.board[7][3].piece = Pawn('black', (3,7), TILE_TO_POS[(3,7)])
        self.board[8][2].piece = Pawn('black', (2,8), TILE_TO_POS[(2,8)])

        # Setting up the white pieces
        self.board[20][0].piece = Bishop('white', (0,20), TILE_TO_POS[(0,20)])
        self.board[19][0].piece = Queen('white', (0,19), TILE_TO_POS[(0,19)])
        self.board[19][1].piece = King('white', (1,19), TILE_TO_POS[(1,19)])
        self.board[18][0].piece = Knight('white', (0,18), TILE_TO_POS[(0,18)])
        self.board[18][1].piece = Bishop('white', (1,18), TILE_TO_POS[(1,18)])
        self.board[18][2].piece = Knight('white', (2,18), TILE_TO_POS[(2,18)])
        self.board[17][0].piece = Rook('white', (0,17), TILE_TO_POS[(0,17)])
        self.board[17][3].piece = Rook('white', (3,17), TILE_TO_POS[(3,17)])
        self.board[16][0].piece = Pawn('white', (0,16), TILE_TO_POS[(0,16)])
        self.board[16][2].piece = Bishop('white', (2,16), TILE_TO_POS[(2,16)])
        self.board[16][4].piece = Pawn('white', (4,16), TILE_TO_POS[(4,16)])
        self.board[15][1].piece = Pawn('white', (1,15), TILE_TO_POS[(1,15)])
        self.board[15][4].piece = Pawn('white', (4,15), TILE_TO_POS[(4,15)])
        self.board[14][1].piece = Pawn('white', (1,14), TILE_TO_POS[(1,14)])
        self.board[14][3].piece = Pawn('white', (3,14), TILE_TO_POS[(3,14)])
        self.board[14][5].piece = Pawn('white', (5,14), TILE_TO_POS[(5,14)])
        self.board[13][2].piece = Pawn('white', (2,13), TILE_TO_POS[(2,13)])
        self.board[13][3].piece = Pawn('white', (3,13), TILE_TO_POS[(3,13)])
        self.board[12][2].piece = Pawn('white', (2,12), TILE_TO_POS[(2,12)])

