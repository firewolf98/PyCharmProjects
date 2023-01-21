def conteggio(f):
    def wrapper(*args, **kwargs):
        C.counter += 1
        f(*args, *kwargs)
    return wrapper


class C:
    counter = 0

    def numinvocazioni():
        return C.counter
    numinvocazioni = staticmethod(numinvocazioni)

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
print(c2.numinvocazioni())