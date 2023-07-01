def Ton(now):
    then = 42 # then is a local variable that won't interfere with the then declared in main.

    def no(know):
        no = then # no is a local variable that won't interfere with the then declared in main.
        return know * now(know)
    return no


if __name__ == '__main__':
    # variable assignments: int then = 7, no = 4
    then, no = 7, 4 
    
    # A lambda function that takes an integer ‘oh’ and returns ‘oh * no’ – ‘4 * oh’ in our case.
    def now(oh): return oh * no
    
    # Ton(now), let’s denote it as TonNow, returns a specialized version of the higher-order function Ton:
    # def TonNow(num):
    #   return num * now(num)
    # We can further inline the now, a lambda expression, and get:
    # def TonNow(num):
    #   return num * (num * 4)
    # Therefore, ok = Ton(now)(no) = TonNow(no) = TonNow(4) = 4 * (4 * 4).
    ok = Ton(now)(no)
    
    # 64
    print(ok)
