def f(arr1, arr2):
    ret = []
    for k in arr1:
        for v in arr2:
            ret.append([k, v])
    return ret


if __name__ == '__main__':
    print(f(['S', 'C'], [1, 2, 3]))
    print(f(['S', 'C'], [3, 2, 1]))
    print(f([], [3, 2, 1]))
    print(f(['S', 'C'], []))
