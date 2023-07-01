x = "x"
g = x


def x(x):  # denoted by globalX
    g = "h"
    if x == g:
        return x + "i"

    def x(x):  # denoted by localX
        return x(g)
    return lambda g: x(g)


if __name__ == "__main__":
    # let's consider x(x)(x) as f = x(x) and x(x)(x) = f(x)
    # f = x(x) = globalX(x = "x"):
    # def x(x = "x"):
    #   g = "h"
    #   if x == g: // evaluates False as "x" != "h"
    #     return x + "i"
    #   def x(x): // NOT to be mixed with GlobalX
    #     return x(g)
    #   // return a lambda expression that effectively returns localX(x = "h") <-> globalX(g = "h")
    #   return lambda g: x(g)
    # Hence, f = x(x) = localX(g == "h") = globalX(g == "h"):
    # This time the if statement if x == g evaluates True.
    # Therefore, f is a function that takes a single parameter x and return x + "i";
    # "hi"
    print(x(x)(x))
