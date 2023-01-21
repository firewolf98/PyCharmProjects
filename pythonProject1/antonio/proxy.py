class MyClass:
    def __init__(self, v):
        self.v = v

    def f(self): print("sono f v = {}".format(self.v))

    def g(self, x, y): print("sono g  x = {} e y = {}".format(x,y))

    def create(self): print("sono create")

    def finalize(self):
        print("sono finalize")

class P:

    def __init__(self, v):
        self.command = []
        self.mc = MyClass(v)

    def f(self):
        self.mc.f()

    def g(self, x, y):
        self.command.append((self.mc.g, x, y))

    def create(self):
        self.command.append(self.mc.create)

    def finalize(self):
        for x in self.command:
            metodo, *args = x
            metodo(*args)
        self.mc.finalize()


p = P(3)
p.f()
p.g(2,3)
p.create()
p.finalize()