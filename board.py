from hexagon import *
from CONST import *
from piece import *

class Board():
    def __init__(self):
        self.board =  [
            [None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None]
        ]
    
    def hexagon_setup(self):
        for key in TILE_TO_POS:
            y, x = key
            hex = Hexagon(key)
            hex.coords = TILE_TO_POS[key]
            self.board[x][y] = hex

    def piece_setup(self):
        self.board[6][5].piece = Knight('white', (5,6), TILE_TO_POS[(5,6)])

        '''
        # Setting up the black pieces
        self.board[0][5].piece = Bishop('black', (5,0), TILE_TO_POS[(5,0)])
        self.board[1][4].piece = Queen('black', (4,1), TILE_TO_POS[(4,1)])
        self.board[1][6].piece = King('black', (6,1), TILE_TO_POS[(6,1)])
        self.board[2][3].piece = Knight('black', (3,2), TILE_TO_POS[(3,2)])
        self.board[2][5].piece = Bishop('black', (5,2), TILE_TO_POS[(5,2)])
        self.board[2][7].piece = Knight('black', (7,2), TILE_TO_POS[(7,2)])
        self.board[3][2].piece = Rook('black', (2,3), TILE_TO_POS[(2,3)])
        self.board[3][8].piece = Rook('black', (8,3), TILE_TO_POS[(8,3)])
        self.board[4][1].piece = Pawn('black', (1,4), TILE_TO_POS[(1,4)])
        self.board[4][5].piece = Bishop('black', (5,4), TILE_TO_POS[(5,4)])
        self.board[4][9].piece = Pawn('black', (9,4), TILE_TO_POS[(9,4)])
        self.board[5][2].piece = Pawn('black', (2,5), TILE_TO_POS[(2,5)])
        self.board[5][8].piece = Pawn('black', (8,5), TILE_TO_POS[(8,5)])
        self.board[6][3].piece = Pawn('black', (3,6), TILE_TO_POS[(3,6)])
        self.board[6][7].piece = Pawn('black', (7,6), TILE_TO_POS[(7,6)]) 
        self.board[7][4].piece = Pawn('black', (4,7), TILE_TO_POS[(4,7)])
        self.board[7][6].piece = Pawn('black', (6,7), TILE_TO_POS[(6,7)])
        self.board[8][5].piece = Pawn('black', (5,8), TILE_TO_POS[(5,8)])

        # Setting up the white pieces
        self.board[20][5].piece = Bishop('white', (5,20), TILE_TO_POS[(5,20)])
        self.board[19][4].piece = Queen('white', (4,19), TILE_TO_POS[(4,19)])
        self.board[19][6].piece = King('white', (6,19), TILE_TO_POS[(6,19)])
        self.board[18][3].piece = Knight('white', (3,18), TILE_TO_POS[(3,18)])
        self.board[18][5].piece = Bishop('white', (5,18), TILE_TO_POS[(5,18)])
        self.board[18][7].piece = Knight('white', (7,18), TILE_TO_POS[(7,18)])
        self.board[17][2].piece = Rook('white', (2,17), TILE_TO_POS[(2,17)])
        self.board[17][8].piece = Rook('white', (8,17), TILE_TO_POS[(8,17)])
        self.board[16][1].piece = Pawn('white', (1,16), TILE_TO_POS[(1,16)])
        self.board[16][5].piece = Bishop('white', (5,16), TILE_TO_POS[(5,16)])
        self.board[16][9].piece = Pawn('white', (9,16), TILE_TO_POS[(9,16)])
        self.board[15][2].piece = Pawn('white', (2,15), TILE_TO_POS[(2,15)])
        self.board[15][8].piece = Pawn('white', (8,15), TILE_TO_POS[(8,15)])
        self.board[14][3].piece = Pawn('white', (3,14), TILE_TO_POS[(3,14)])
        self.board[14][7].piece = Pawn('white', (7,14), TILE_TO_POS[(7,14)])
        self.board[13][4].piece = Pawn('white', (4,13), TILE_TO_POS[(4,13)])
        self.board[13][6].piece = Pawn('white', (6,13), TILE_TO_POS[(6,13)])
        self.board[12][5].piece = Pawn('white', (5,12), TILE_TO_POS[(5,12)])
        '''