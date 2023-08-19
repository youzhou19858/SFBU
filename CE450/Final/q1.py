def trc1(g):
    def inner(num):
        x = g(num)
        return x
    return inner


@trc1
def sqr(x):
    return x*x


@trc1
def sum_sqr(n):
    ret = 0
    for i in range(n, 0, -1):
        ret += sqr(i)
    return ret


if __name__ == "__main__":
    print(sqr(3))
    print(sum_sqr(3))
