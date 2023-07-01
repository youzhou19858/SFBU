def horn(hood):
    horn = hood

    def hood(horn):
        return horn
    return horn(hood)


if __name__ == '__main__':
    # function hood takes in any callable, denoted by func, as the only parameter
    # and returns the result of the callable parameterized with a constant integer 2, namely func(2)
    # let's also denoted function hood by fWith2
    def hood(horn): return horn(2)

    # Then horn(hood) <--> horn(fWith2):
    # def horn(hood = fWith2):
    #   horn = hood // horn = fWith2 effectively
    #   def hood(horn):
    #     return horn
    #   return horn(hood) // return fWith2(hood // the local definition)
    # fWith2(hood) <--> hood(2) <-> return the result of hood parameterized with a constant integer 2:
    #   def hood(horn = 2):
    #     return horn // return 2
    print(horn(hood))
