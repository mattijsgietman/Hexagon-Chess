class Piece:
    def __init__(self, color, position, coords):
        self.color = color
        self.position = position
        self.coords = coords


class Pawn(Piece):
    def __init__(self, color, position, coords):
        super().__init__(color, position, coords)
        self.name = 'pawn'
        self.has_moved = False


class Knight(Piece):
    def __init__(self, color, position, coords):
        super().__init__(color, position, coords)
        self.name = 'knight'


class Bishop(Piece):
    def __init__(self, color, position, coords):
        super().__init__(color, position, coords)
        self.name = 'bishop'


class Rook(Piece):
    def __init__(self, color, position, coords):
        super().__init__(color, position, coords)
        self.name = 'rook'


class Queen(Piece):
    def __init__(self, color, position, coords):
        super().__init__(color, position, coords)
        self.name = 'queen'


class King(Piece):
    def __init__(self, color, position, coords):
        super().__init__(color, position, coords)
        self.name = 'king'
    
