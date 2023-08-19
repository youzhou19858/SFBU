def verify_add(m, ls):
    """Returns True if addition of any two different elements in ls is m.
    >>> verify_add (100, [1, 2, 3, 4, 5])
    False
    >>> verify_add (7, [1, 2, 3, 4, 2])
    True # 7 = 3 +4
    >>> verify_add (10, [5, 5])
    False
    >>> verify_add (151, range(0, 200000, 3))
    False
    >>>verify_add(50004, range(0, 200000, 4))
    True # 50004 = 50000 + 4
    """
    """ YOUR SOURCE CODE HRER """
    added = set()
    for a in ls:
        b = m - a
        if a != b and b in added:
            return True
        added.add(a)
    return False


if __name__ == "__main__":
    print(verify_add(100, [1, 2, 3, 4, 5]))
    print(verify_add(7, [1, 2, 3, 4, 2]))
    print(verify_add(10, [5, 5]))
    print(verify_add(151, range(0, 200000, 3)))
    print(verify_add(50004, range(0, 200000, 4)))
