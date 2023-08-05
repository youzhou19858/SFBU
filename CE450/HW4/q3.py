from link import link
from q2 import printLinkList


def reverseLinkList(ll: link):
    prev: link = None
    while ll:
        prev = link(ll.ele, prev)
        ll = ll.next
    return prev


if __name__ == '__main__':
    printLinkList(reverseLinkList(link(1, link(2, link(3, link(4))))))
