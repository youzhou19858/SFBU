from link import link


def printLinkList(ll: link):
    while ll:
        print(f'{ll.ele} ', end='')
        ll = ll.next


if __name__ == '__main__':
    printLinkList(link(1, link(2, link(3, link(4)))))
