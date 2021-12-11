class even:
    def __init__(self, max):
        self.n = 2
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.max:
            result = self.n
            self.n += 2
            return result
        else:
            raise StopIteration


e = even(10)
print(next(e))
print(next(e))
print(next(e))
print(next(e))
print(next(e))
print(next(e))
