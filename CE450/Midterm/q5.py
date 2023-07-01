pear = "ni"


def apple(banana):
    def plum(peach):
        def pear(pear): return peach(pear)
        return pear
    return plum(banana)("ck")


if __name__ == "__main__":
    # Let's denoted the lambda expression lambda peach: pear + peach by concatenate.
    # concatenate basically takes a single variable peach and append peach to the back of the global variable pear.
    # Then apple(lambda peach: pear + peach) = apple(concatenate):
    # def apple(banana = concatenate):
    #   def plum(peach):
    #     def pear(pear): return peach(pear)
    #     return pear
    #   return plum(banana = concatenate)("ck")
    # where plum(banana = concatenate) =
    #   def plum(peach = concatenate):
    #     def pear(pear):
    #       return peach(pear) // return concatenate(pear)
    #     return pear // return concatenate(pear)
    # Therefore, plum(banana = concatenate)("ck") <--> concatenate(pear = "ck") <--> append "ck" to the back of "ni" <--> "nick"
    print(apple(lambda peach: pear + peach))
