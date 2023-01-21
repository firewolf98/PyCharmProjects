def conteggio(f):
    def wrapper(self):
        self.counter = self.counter + 1
        return f
    return wrapper


class C:
    counter = 0

    def numinvocazioni(self):
        return self.counter

    @conteggio
    def m1(self):
        print("m1")

    @conteggio
    def m2(self):
        print("m2")


c = C();
print(c.numinvocazioni())
c.m1()
c.m1()
c.m2()
print(c.numinvocazioni())
c2 = C();
c2.m1()
print(c2.numinvocazioni())


