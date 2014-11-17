from Move import Move
from Type import Type

class Struggle(Move):
    ''' Represents the struggle move. It's upper class is Move. The only difference is use_move method wich in Stuggle, is a simple pass
    '''
    def __init__(self):
        super().__init__("struggle", Type.Normal, 100, 50, 1)

    def use_move(self):
        pass
