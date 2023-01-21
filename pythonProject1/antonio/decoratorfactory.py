def decFact(name):
    def makeCounter(cls):
        cls.contatore = 0
        f = getattr(cls, name)
        def conta(self):
            cls.contatore += 1
            f(self)
        def returnCounter():
            return cls.contatore
        returnCounter = staticmethod(returnCounter)
        setattr(cls, name, conta)
        setattr(cls, "returnCounter", returnCounter)
        return cls
    return makeCounter

@decFact("m1")
class C:

    def m2(self):
        print("m2")

    def m1(self):
        print("m1")


c = C()
c.m2()
c.m2()
c.m1()
print(C.returnCounter())

print(dict.__dict__)
