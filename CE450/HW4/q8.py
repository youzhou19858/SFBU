from link import link
from q2 import printLinkList


def insert(ll: link, ele, ind):
    head = link(-1, ll)
    ret = head
    for _ in range(ind):
        if not head.next:
            break
        head = head.next
    nnext = head.next
    head.next = link(ele)
    head.next.next = nnext
    return ret.next


if __name__ == '__main__':
    l = link(11, link(12, link(13)))
    n = insert(l, 2021, 1)
    printLinkList(n)
    print()
    m = insert(n, 2022, 20)
    printLinkList(m)
