
def square(x):
    return x * x


def triple(x):
    return x * 3


def increment(x):
    return x + 1


def identity(x):
    return x


def intscts(f, x):
    def takeG(g):
        return g(x) == f(x)
    return takeG


if __name__ == '__main__':
    at_three = intscts(square, 3)
    print(at_three(triple))
    print(at_three(increment))
    at_one = intscts(identity, 1)
    print(at_one(square))
    print(at_one(triple))
