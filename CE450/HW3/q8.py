from typing import List


def isSymmetrical(arr: List):
    if not arr:
        return True
    if arr[0] != arr[-1]:
        return False
    return isSymmetrical(arr[1:len(arr) - 1])


if __name__ == '__main__':
    print(isSymmetrical([]))
    print(isSymmetrical([1]))
    print(isSymmetrical([1, 4, 5, 1]))
    print(isSymmetrical([1, 4, 4, 1]))
    print(isSymmetrical(['l', 'o', 'l']))
