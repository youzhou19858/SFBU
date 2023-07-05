def addXManyElements(x, element, arr):
    for _ in range(x):
        arr.append(element)
    return arr


if __name__ == '__main__':
    arr = [1, 2, 4, 2, 1]
    print(addXManyElements(2, 5, arr))
