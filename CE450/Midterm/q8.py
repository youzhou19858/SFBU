from math import floor, log10


def isPalindrome(x: int):
    if x < 0:
        return False
    if x < 10:
        return True

    def check(nStr: str) -> bool:
        if not nStr:
            return True
        if nStr[0] != nStr[-1]:
            return False
        return check(nStr[1:len(nStr) - 1])
    return check(str(x))


if __name__ == "__main__":
    print(isPalindrome(45654))
    print(isPalindrome(42))
    print(isPalindrome(2019))
    print(isPalindrome(10101))
