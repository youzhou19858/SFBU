def identity(x):
    return x


def square(x):
    return x * x


def adder(f1, f2):
    def func(x: int):
        return f1(x) + f2(x)
    return func


if __name__ == '__main__':
    a1 = adder(identity, square)
    print(a1(4))
    a2 = adder(a1, identity)
    print(a2(4))
    print(a2(5))
    a3 = adder(a1, a2)
    print(a3(4))
