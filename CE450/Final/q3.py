def deep_rvrs(tup):
    """Reverses tuple with possible tuple elements
    >>> a = (11, 12, 13, 14)
    >>> deep_rvrs (a)
    (14, 13, 12, 11)
    >>>tpl = (11, (12, (13,113), 14), 15)
    >>> deep_rvrs (tpl)
    (15, (14, (113, 13), 12), 11))
    """
    """ YOUR SOURCE CODE HRER """
    ret = tuple()
    for i in range(len(tup) - 1, -1, -1):
        if isinstance(tup[i], tuple):
            ret += (deep_rvrs(tup[i]),)
        else:
            ret += (tup[i],)
    return ret


if __name__ == "__main__":
    print(deep_rvrs((11, 12, 13, 14)))
    print(deep_rvrs((11, (12, (13, 113), 14), 15)))
