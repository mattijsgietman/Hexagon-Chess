from hexagon import *
from CONST import *
from piece import *

class Board():
    def __init__(self):
        self.board =  [
            [None, None, None, None, None, None],
            [None, None, None, None, None, None],
            [None, None, None, None, None, None],
            [None, None, None, None, None, None],
            [None, None, None, None, None, None],
            [None, None, None, None, None, None],
            [None, None, None, None, None, None],
            [None, None, None, None, None, None],
            [None, None, None, None, None, None],
            [None, None, None, None, None, None],
            [None, None, None, None, None, None],
            [None, None, None, None, None, None],
            [None, None, None, None, None, None],
            [None, None, None, None, None, None],
            [None, None, None, None, None, None],
            [None, None, None, None, None, None],
            [None, None, None, None, None, None],
            [None, None, None, None, None, None],
            [None, None, None, None, None, None],
            [None, None, None, None, None, None],
            [None, None, None, None, None, None]
        ]
    
    def hexagon_setup(self):
        for key in TILE_TO_POS:
            y, x = key
            hex = Hexagon(key)
            hex.coords = TILE_TO_POS[key]
            self.board[x][y] = hex

    def piece_setup(self):
        # Setting up the black pieces
        self.board[0][3].piece = Bishop('black', (3,0), TILE_TO_POS[(3,0)])
        self.board[1][2].piece = Queen('black', (2,1), TILE_TO_POS[(2,1)])
        self.board[1][3].piece = King('black', (3,1), TILE_TO_POS[(3,1)])
        self.board[2][2].piece = Knight('black', (2,2), TILE_TO_POS[(2,2)])
        self.board[2][3].piece = Bishop('black', (3,2), TILE_TO_POS[(3,2)])
        self.board[2][4].piece = Knight('black', (4,2), TILE_TO_POS[(4,2)])
        self.board[3][1].piece = Rook('black', (1,3), TILE_TO_POS[(1,3)])
        self.board[3][4].piece = Rook('black', (4,3), TILE_TO_POS[(4,3)])
        self.board[4][1].piece = Pawn('black', (1,4), TILE_TO_POS[(1,4)])
        self.board[4][3].piece = Bishop('black', (3,4), TILE_TO_POS[(3,4)])
        self.board[4][5].piece = Pawn('black', (5,4), TILE_TO_POS[(5,4)])
        self.board[5][1].piece = Pawn('black', (1,5), TILE_TO_POS[(1,5)])
        self.board[5][4].piece = Pawn('black', (4,5), TILE_TO_POS[(4,5)])
        self.board[6][2].piece = Pawn('black', (2,6), TILE_TO_POS[(2,6)])
        self.board[6][4].piece = Pawn('black', (4,6), TILE_TO_POS[(4,6)]) 
        self.board[7][2].piece = Pawn('black', (2,7), TILE_TO_POS[(2,7)])
        self.board[7][3].piece = Pawn('black', (3,7), TILE_TO_POS[(3,7)])
        self.board[8][3].piece = Pawn('black', (3,8), TILE_TO_POS[(3,8)])

        # Setting up the white pieces
        self.board[20][3].piece = Bishop('white', (3,20), TILE_TO_POS[(3,20)])
        self.board[19][2].piece = Queen('white', (2,19), TILE_TO_POS[(2,19)])
        self.board[19][3].piece = King('white', (3,19), TILE_TO_POS[(3,19)])
        self.board[18][2].piece = Knight('white', (2,18), TILE_TO_POS[(2,18)])
        self.board[18][3].piece = Bishop('white', (3,18), TILE_TO_POS[(3,18)])
        self.board[18][4].piece = Knight('white', (4,18), TILE_TO_POS[(4,18)])
        self.board[17][1].piece = Rook('white', (1,17), TILE_TO_POS[(1,17)])
        self.board[17][4].piece = Rook('white', (4,17), TILE_TO_POS[(4,17)])
        self.board[16][1].piece = Pawn('white', (1,16), TILE_TO_POS[(1,16)])
        self.board[16][3].piece = Bishop('white', (3,16), TILE_TO_POS[(3,16)])
        self.board[16][5].piece = Pawn('white', (5,16), TILE_TO_POS[(5,16)])
        self.board[15][1].piece = Pawn('white', (1,15), TILE_TO_POS[(1,15)])
        self.board[15][4].piece = Pawn('white', (4,15), TILE_TO_POS[(4,15)])
        self.board[14][2].piece = Pawn('white', (2,14), TILE_TO_POS[(2,14)])
        self.board[14][4].piece = Pawn('white', (4,14), TILE_TO_POS[(4,14)])
        self.board[13][2].piece = Pawn('white', (2,13), TILE_TO_POS[(2,13)])
        self.board[13][3].piece = Pawn('white', (3,13), TILE_TO_POS[(3,13)])
        self.board[12][3].piece = Pawn('white', (3,12), TILE_TO_POS[(3,12)])

