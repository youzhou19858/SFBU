from typing import List


def checkIfElementIn(element, arr: List):
    if not arr:
        return False
    elif type(arr[0]) == list:
        return checkIfElementIn(element, arr[0]) or checkIfElementIn(element, arr[1:])
    else:
        return arr[0] == element or checkIfElementIn(element, arr[1:])


if __name__ == '__main__':
    print(checkIfElementIn(6,  [[1, [2]], 3, [[4], [5, [6]]]]))
