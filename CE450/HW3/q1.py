def account(balance):
    def withdraw(amount: float):
        nonlocal balance
        if amount <= balance:
            balance -= amount
            return balance
        else:
            return 'Insufficient Funds'
    return withdraw


if __name__ == '__main__':
    acct = account(100)
    print(acct(10))
    print(acct(20))
    print(acct(100))
