class MoveListEnumerator:
    def __init__(self, lst):
        self._lst = lst
        self._idx = 1

    def __iter__(self):
        return self

    def __next__(self):
        try:
            result = self._lst[self._idx]
        except IndexError:
            self._idx = 1
            raise StopIteration
        self._idx += 1
        return self._idx - 1, result
