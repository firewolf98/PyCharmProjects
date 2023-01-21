class Base:
    def __init__(self, a, b):
        self.a = a
        self.b = b


    def stampa(self):
        print("<{0}>,<{1}>".format(self.a, self.b))


class Derivata(Base):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c


    def stampa(self):
        print("[{0}]-[{1}]".format(self.a, self.b))


b = Base(1, 3)
b.stampa()
d = Derivata("a", "b", 9)
d.stampa()
