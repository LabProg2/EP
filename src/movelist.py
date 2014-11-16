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

        # isso ta errado... eu tenho que consertar no iterator pra só devolver coisas que não são struggle
        if len(moves) == 1 and isinstance(moves[0], MoveList):
            for move in moves[0]:
                move_list.append(move)

        else:
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
        self._index = 1

    def __iter__(self):
        # return iter(self.moves)
        return self

    def __next__(self):
        try:
            result = self._moves[self._index]
        except IndexError:
            self._index = 1
            raise StopIteration
        self._index += 1
        return result

    def __len__(self):
        return len(self._moves) - 1

    def add_move(self, move):
        if len(self._moves) < self._max_moves:
            self._moves.append(move)
        else:
            raise OverflowError("movelist is full")

    def get_move(self, n):
        try:
            return self._moves[n + 1]
        except IndexError:
            return None

    def get_move_id(self, move):
        for i in range(self._max_moves):
            if move == self._moves[i + 1]:
                return i + 1

    def has_available_moves(self):
        for move in self._moves:
            if move.isavailable():
                return True
        return False
    
