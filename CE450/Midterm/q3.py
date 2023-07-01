# a global variable not to be interfered with local variables declared with the same name.
woo = 6


def much(woo):
    # python compares functions effectively by comparing their id() -- pointer basically.
    if much == woo:
        def such(woo):
            return 5

        def woo():
            return such
        return woo

    def such(woo):
        return 4
    return woo()


if __name__ == '__main__':
    # let's first denote much by m, much(much) by mm, and much(much(much)) by mmm.
    # then, we see mmm = m(mm), and
    # Since python compares functions effectively by comparing their id() -- pointer basically,
    # the if much == woo statement when specializing mm will evaluate True.
    # Hence, effectively we only need to consider this if block for mm:
    # if much == woo:
    #     def such(woo):
    #         return 5
    #     def woo():
    #         return such
    #     return woo
    # By tracing, we see mm <- return (woo <- return (such <- return 5)) <--> mm <- return 5.
    # Noticing that mm is NOT an integer! To be precisely, mm is a function that returns a constant integer 5.
    # Now mmm = m(mm) = m(a function that returns a constant integer 5)
    # Since the if much == woo statement evaluates False for mmm,
    # we only need to consider block:
    # def much(woo):
    #     def such(woo):
    #         return 4
    #      return woo()
    # Hence, mmm = = m(mm) = m(a function that returns a constant integer 5) = a function that returns a constant integer 5
    # woo = much(much(much))(woo) <--> woo = mmm(6) <--> woo = 5
    woo = much(much(much))(woo)
    # 5
    print(woo)
