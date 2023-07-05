from typing import List


def flatten(arr: List):
    if not arr:
        return []
    elif type(arr[0]) == list:
        return flatten(arr[0]) + flatten(arr[1:])
    else:
        return [arr[0]] + flatten(arr[1:])


if __name__ == '__main__':
    print("flatten([1,2,[3,4,[5,6]]]):", flatten([1, 2, [3, 4, [5, 6]]]))
    print("flatten([1,2,3]:", flatten([1, 2, 3]))
    print("flatten([1,[2,3],4]:", flatten([1, [2, 3], 4]))
    print("flatten([1,[2,[3,4],5],6]):", flatten([1, [2, [3, 4], 5], 6]))
    print("flatten([[1, [1, 1]], 1, [1, 1]]):",
          flatten([[1, [1, 1]], 1, [1, 1]]))
