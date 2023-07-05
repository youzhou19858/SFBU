
def create2DArr(row: int, col: int):
    return [['-' for _ in range(col)] for _ in range(row)]


if __name__ == '__main__':
    print(create2DArr(3, 5))
