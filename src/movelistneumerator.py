class MoveListEnumerator:
    def __init__(self, lst):
        self._lst = lst
        self._idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            result = self._lst[idx]
        except IndexError:
            raise StopIteration
        self._idx += 1
        return self._idx, result
