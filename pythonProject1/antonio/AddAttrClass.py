class clsBase:
    def addAttr(self, s, v):
        try:
            getattr(self, s)
        except AttributeError:
            setattr(self, s, v)


class clsExt(clsBase):
    pass


c = clsBase()
c.addAttr("aaa", 4)
print(c.aaa)
x = clsExt()
x.addAttr("aaa", 4)
print(x.aaa)