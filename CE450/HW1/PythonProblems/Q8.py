def adjacentFive(n: int, last: int = 0) -> bool:
    while (n):
        curr = n % 10
        if curr == last == 5:
            return True
        last = curr
        n //= 10
    return False

if __name__ == "__main__":
    print(adjacentFive(5))
    print(adjacentFive(55))
    print(adjacentFive(550055))
    print(adjacentFive(12345))
    print(adjacentFive(50505050))