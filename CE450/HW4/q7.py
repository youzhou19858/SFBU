from link import link
from q2 import printLinkList


def append(ll: link, m):
    ret = ll
    while ll.next:
        ll = ll.next
    ll.next = link(m)
    return ret


if __name__ == '__main__':
    l = link(1, link(2, link(3)))
    n = append(l, 4)
    printLinkList(n)
