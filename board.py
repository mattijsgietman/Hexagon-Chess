from hexagon import *
from CONST import *

class Board():
    def __init__(self):
        self.board =  [
            [None],
            [None, None],
            [None, None, None],
            [None, None, None, None],
            [None, None, None, None, None],
            [None, None, None, None, None, None],
            [None, None, None, None, None],
            [None, None, None, None, None, None],
            [None, None, None, None, None],
            [None, None, None, None, None, None],
            [None, None, None, None, None],
            [None, None, None, None, None, None],
            [None, None, None, None, None],
            [None, None, None, None, None, None],
            [None, None, None, None, None],
            [None, None, None, None, None, None],
            [None, None, None, None, None],
            [None, None, None, None],
            [None, None, None,],
            [None, None],
            [None]
        ]
        self.hexagon_setup()
    
    def hexagon_setup(self):
        for key in TILE_TO_POS:
            y, x = key
            hex = Hexagon(key)
            hex.coords = TILE_TO_POS[key]
            self.board[x][y] = hex

    def piece_setup(self):
        pass

