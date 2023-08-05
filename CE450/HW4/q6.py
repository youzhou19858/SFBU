from link import link
from q2 import printLinkList


def change(ll: link, u, v):
    ret = ll
    while ll:
        if ll.ele == u:
            ll.ele = v
        ll = ll.next
    return ret


if __name__ == '__main__':
    l = link(1, link(2, link(3)))
    n = change(l, 3, 1)
    printLinkList(n)
    print()
    m = change(n, 1, 2)
    printLinkList(m)
    print()
    printLinkList(change(m, 5, 1))
