from collections import deque


def add_one(x):
    return x + 1


def times_two(x):
    return x * 2


def add_three(x):
    return x + 3


def cyc(g1, g2, g3):
    def func(n):
        dq = deque([g1, g2, g3])

        def takeX(x):
            for _ in range(n):
                f = dq.popleft()
                x = f(x)
                dq.append(f)
            return x
        return takeX
    return func


if __name__ == '__main__':
    my_cyc = cyc(add_one, times_two, add_three)
    h = my_cyc(0)
    print(h(5))
    # 5
    h = my_cyc(2)
    print(h(1))
    # times_two (add_one (1))
    # 4
    h = my_cyc(3)
    print(h(2))
    # add_three (times_two (add_one (2)))
    # 9
    h = my_cyc(4)
    print(h(2))
    # add_one (add_three (times_two (add_one (2))))
    # 10
    h = my_cyc(6)
    print(h(1))
    # add_three(times_two (add_one (add_three (times_two (add_one (1))))))
    # 19
