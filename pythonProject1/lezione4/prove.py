def provea():
    a = int(3)
    b = int(4)
    print(a.__pow__(b))
    print(a.__rpow__(b))


provea()


class C:
    def __call__(self, *args, **kwargs):
        print('Chiamata:', args, kwargs)


x = C()
x(1, 2, 3)
x(1, 2, 3, x=4, y=5)
