def if_function(condition=True, true_result=True, false_result=True):
    if condition:
        return true_result
    return false_result


if __name__ == "__main__":
    print(if_function(True, 2, 3))
    print(if_function(False, 2, 3))
    print(if_function(3 == 2, 3+2, 3-2))
    print(if_function(3 > 2, 3+2, 3-2))
    print(if_function())
