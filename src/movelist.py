from Move import Move

class MoveList:
    def __init__(self, *moves, max_moves = 4):
        ''' Initializate a list with *max_moves* *moves* '''
        move_list = moves[:max_moves]
        for move in move_list:
            if not isinstance(move, Move):
                raise TypeError("The arguments must be instances of Move")
        self._moves = move_list

    def __iter__(self):
        return iter(self.moves)

    def getMove(self, n):
        try:
            return self._moves[n]
        except IndexError:
            return None

    
