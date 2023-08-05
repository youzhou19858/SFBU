from link import link


def inList(s: link, ele):
    while s:
        if s.ele == ele:
            return True
        s = s.next
    return False


if __name__ == '__main__':
    print(inList(link(1, link(2, link(3))), 1))
    print(inList(link(1, link(2, link(3))), 4))
