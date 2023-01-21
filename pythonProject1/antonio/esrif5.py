def classCounter(name):
    def clsCounter(cls):
        cls.ncall = 0
        setattr(cls, "old", getattr(cls, name))
        def newMeth(self):
            getattr(cls, "old")(self)
            cls.ncall += 1

        def getcall():
            return cls.ncall

        getcall = staticmethod(getcall)
        setattr(cls, "getcall", getcall)
        setattr(cls, name, newMeth)
        return cls
    return clsCounter


@classCounter("meth1")
class C:
    def meth1(self):
        print("meth1")

    def meth2(self):
        print("meth2")

c = C()
print(c.getcall())
c.meth1()
print(C.getcall())
