class Student:
    def __init__(self, name, cnt) -> None:
        self.name = name
        self.cnt = cnt

    def __add__(self, __value: object):
        return Student("dummy", self.cnt + __value.cnt)

    def __str__(self):
        return str(self.cnt)

    def __repr__(self) -> str:
        return self.__str__()

    def __lt__(self, __value: object):
        return self.cnt < __value.cnt

    def __eq__(self, __value: object):
        return self.cnt == __value.cnt

    def __ne__(self, __value: object) -> bool:
        return self.cnt != __value.cnt

    def __gt__(self, __value: object) -> bool:
        return self.cnt > __value.cnt


if __name__ == "__main__":
    a = Student('Peter', 3)
    b = Student('Mike', 4)
    c = Student('John', 5)
    d = Student('Kelvin', 3)
    print(a + b + d)
    print(a != d)
    print(b < c)
    print(c > d)
    print(a == d)
