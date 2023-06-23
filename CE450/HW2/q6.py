def f():
    def ff():
        def fff(x):
            def ffff():
                return x
            return ffff
        return fff
    return ff


if __name__ == '__main__':
    print(f()()(3)())
