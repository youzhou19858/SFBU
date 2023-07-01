def hasSublist(lhs: list[int], rhs: list[int]) -> bool:
    N, M = len(lhs), len(rhs)
    if M == 0:
        return True
    if N < M:
        return False
    headOfRhs = rhs[0]
    try:
        idx = lhs.index(headOfRhs)
        return hasSublist(lhs[idx + 1:], rhs[1:])
    except ValueError:
        return False


if __name__ == "__main__":
    print(hasSublist([], []))
    print(hasSublist([3, 3, 2, 1], []))
    print(hasSublist([], [3, 3, 2, 1]))
    print(hasSublist([3, 3, 2, 1], [3, 2, 1]))
    print(hasSublist([3, 2, 1], [3, 2, 1]))
