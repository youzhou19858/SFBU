def removeAllOccurrences(element, arr):
    return [ele for ele in arr if ele != element]


if __name__ == '__main__':
    x = [3, 1, 2, 1, 5, 1, 1, 7]
    print(removeAllOccurrences(1, x))
