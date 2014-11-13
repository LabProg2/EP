from Move import Move
from Type import Type

class MoveList:
    def __init__(self, *moves, max_moves = 4):
        ''' Initializate a list with *max_moves* *moves* '''
        if max_moves < 0:
            raise ValueError("max_moves must be greater or equal to 0")

        move_list = []
        move_list.append(Move("struggle", Type.Normal, 100, 50, 1))
        max_moves += 1 # Struggle

        for arg in moves:
            if isinstance(arg, MoveList):
                for move in arg:
                    move_list.append(move)
            elif isinstance(arg, list):
                for move in arg:
                    if isinstance(move, Move):
                        move_list.append(move)
            elif isinstance(arg, Move):
                move_list.append(arg)
            else:
                pass

        self._max_moves = max_moves
        self._moves = move_list[:max_moves]
        self._index = 0

    def __iter__(self):
        # return iter(self.moves)
        return self

    def __next__(self):
        try:
            result = self._moves[self._index]
        except IndexError:
            self._index = 0
            raise StopIteration
        self._index += 1
        return result

    def __len__(self):
        return len(self._moves)

    def add_move(self, move):
        if len(self._moves) < self._max_moves:
            self._moves.append(move)
        else:
            raise OverflowError("movelist is full")

    def get_move(self, n):
        try:
            return self._moves[n]
        except IndexError:
            return None

    def has_available_moves(self):
        for move in self._moves[1:]:
            if move.isavailable():
                return True
        return False
    
