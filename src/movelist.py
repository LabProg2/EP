from Move import Move
from Type import Type
from movelistenumerator import MoveListEnumerator

class MoveList:
    def __init__(self, *moves, max_moves = 4):
        ''' Initializate a list with *max_moves* *moves* '''
        if max_moves < 0:
            raise ValueError("max_moves must be greater or equal to 0")


        move_list = []

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
        self._struggle = Move("struggle", Type.Normal, 100, 50, 1)
        self._index = 0

    @property
    def struggle(self):
        return self._struggle    

    def __iter__(self):
        return iter(self._moves)
        # return self

    def enumerate(self):
        ''' Method to iter with indexes 
        :reutrns: an iterable class
        '''
        return MoveListEnumerator(self._moves)

    def __len__(self):
        return len(self._moves)

    def __enumerate__(self):
        return "OOO"

    def add_move(self, move):
        if len(self._moves) < self._max_moves:
            self._moves.append(move)
        else:
            raise OverflowError("movelist is full")

    def get_move(self, n):
        if n < 1:
            return None

        try:
            return self._moves[n - 1]
        except IndexError:
            return None

    def get_move_id(self, move):
        # self._moves.index(move)
        for i in range(self._max_moves):
            if move == self._moves[i]:
                return i 

    def is_move_available(self, index):
        if not self.get_move(index):
            return False
        else:
            return self.get_move(index).isavailable()


    def has_available_moves(self):
        for move in self._moves:
            if move.isavailable():
                return True
        return False
    
