from operator import add, neg


def combine_funcs(op):
    def combined(f, g):
        def val(x):
            return op(f(x), g(x))
        return val
    return combined


if __name__ == '__main__':
    add_func = combine_funcs(add)
    # add_func =
    #     def combined(f, g):
    #         def val(x):
    #             return add(f(x), g(x))
    #         return val
    h = add_func(abs, neg)
    # h =
    #         def val(x):
    #             return add(abs(x), neg(x))
    print(h(-5))
