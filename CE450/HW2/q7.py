def square(x):
    return x * x


def smth(g, dx):
    return lambda x: (g(x - dx) + g(x) + g(x + dx)) / 3


if __name__ == '__main__':
    print(round(smth(square, 1)(0), 3))
