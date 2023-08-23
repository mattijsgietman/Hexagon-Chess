class Move:
    def __init__(self, piece, initial, target):
        self.piece = piece
        self.initial = initial
        self.target = target

    def __eq__(self, other):
        return self.initial == other.initial and self.target == other.target