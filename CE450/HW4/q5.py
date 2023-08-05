from link import link


def sumLL(ll: link, g):
    ret = 0
    while ll:
        ret += g(ll.ele)
        ll = ll.next
    return ret


if __name__ == '__main__':
    def sqr(x): return x * x
    def dbl(y): return 2 * y
    lnk1 = link(1, link(2, link(3, link(4))))
    print(sumLL(lnk1, sqr))
    lnk2 = link(3, link(5, link(4, link(6))))
    print(sumLL(lnk2, dbl))
