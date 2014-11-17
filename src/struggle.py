from Move import Move
from Type import Type

class Struggle(Move):
    def __init__(self):
        super().__init__("struggle", Type.Normal, 100, 50, 1)

    def use_move(self):
        pass
