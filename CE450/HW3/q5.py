from typing import List


def mergeTwoSortedList(arr1: List, arr2: List) -> List:
    if not arr1:
        return arr2
    if not arr2:
        return arr1
    ret = []
    if arr1[0] <= arr2[0]:
        ret.append(arr1[0])
        ret.extend(mergeTwoSortedList(arr1[1:], arr2))
    else:
        ret.append(arr2[0])
        ret.extend(mergeTwoSortedList(arr1, arr2[1:]))
    return ret


if __name__ == '__main__':
    print(mergeTwoSortedList([1, 3, 5], [2, 4, 6]))
    print(mergeTwoSortedList([], [2, 4, 6]))
    print(mergeTwoSortedList([1, 2, 3], []))
    print(mergeTwoSortedList([5, 7], [2, 4, 6]))
