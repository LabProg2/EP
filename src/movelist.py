from Move import Move
from struggle import Struggle
from Type import Type
from movelistenumerator import MoveListEnumerator

class MoveList:
    def __init__(self, *moves, max_moves = 4):
        ''' Initializate a list with *max_moves* *moves* '''
        if max_moves < 0:
            raise ValueError("max_moves must be greater or equal to 0")


        move_list = []
        move_list.append(Struggle())

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
        self._moves = move_list[:max_moves + 1]
        self._index = 1

    @property
    def struggle(self):
        return self._moves[0]

    def __iter__(self):
        # return iter(self._moves)
        return self

    def __next__(self):
        try:
            result = self._moves[self._index]
        except IndexError:
            self._index = 1
            raise StopIteration
        self._index += 1
        return result

    def enumerate(self):
        ''' Method to iter with indexes 
        :reutrns: an iterable class
        '''
        return MoveListEnumerator(self._moves)

    def __len__(self):
        return len(self._moves) - 1

    def add_move(self, move):
        if len(self) < self._max_moves:
            self._moves.append(move)
        else:
            raise OverflowError("movelist is full")

    def get_move(self, n):
        if n < 0:
            return None

        try:
            return self._moves[n]
        except IndexError:
            return None

    def get_move_id(self, move):
        # self._moves.index(move)
        for i in range(len(self._moves)):
            if move == self._moves[i]:
                return i 
        return None

    def is_move_available(self, index):
        if not self.get_move(index) or (index == 0 and self.has_available_moves()):
            return False
        else:
            return self.get_move(index).isavailable()


    def has_available_moves(self):
        for move in self._moves[1:]:
            if move.isavailable():
                return True
        return False
    
