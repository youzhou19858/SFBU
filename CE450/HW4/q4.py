from link import link


def isSorted(ll: link):
    prev = ll.ele
    ll = ll.next
    while ll:
        if prev > ll.ele:
            return False
        prev = ll.ele
        ll = ll.next
    return True


if __name__ == '__main__':
    print(isSorted(link(1, link(2, link(3, link(4))))))
    print(isSorted(link(1, link(3, link(2, link(4, link(5)))))))
    print(isSorted(link(3, link(3, link(3)))))
