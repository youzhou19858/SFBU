class Fibonacci:
    def __init__(self):
        self.val = 0
        self.prev = 1

    def nxt(self):
        """ YOUR SOURCE CODE HRER """
        temp = self.val
        self.val += self.prev
        self.prev = temp
        return self

    def __repr__(self):
        temp = self.val
        self.val = 0
        self.prev = 1
        return str(temp)


if __name__ == "__main__":

    """A Fibonacci number.
    >>> a = Fibonacci():
    >>> a
    0
    >>> a.nxt()
    1
    >>> a.nxt().nxt()
    1
    >>> a.nxt().nxt().nxt()
    2
    >>> a.nxt().nxt().nxt().nxt()
    3
    >>> a.nxt().nxt().nxt().nxt().nxt()
    5
    >>> a.nxt().nxt().nxt().nxt().nxt().nxt()
    8
    """
    a = Fibonacci()
    print(a)
    print(a.nxt())
    print(a.nxt().nxt())
    print(a.nxt().nxt().nxt())
    print(a.nxt().nxt().nxt().nxt())
    print(a.nxt().nxt().nxt().nxt().nxt())
    print(a.nxt().nxt().nxt().nxt().nxt().nxt())
