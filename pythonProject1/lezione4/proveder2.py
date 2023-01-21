class base():
    def f(self):
        print("base")


class der(base):
    def f(self):
        print("der")


    def g(self):
        self.f()
        super().f()
        super(der, self).f()
        base.f(self)


class derder(der):
    def f(self):
        print("derder")


    def h(self):
        self.f()
        super().f()
        super(derder, self).f()
        super(der, self).f()


x = der()
x.g()
y = derder()
y.h()
