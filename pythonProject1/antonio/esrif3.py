class clsBase():
    def addAttr(self, s, v):
        try:
            getattr(self, s)
        except:
            setattr(self,s,v)

c = clsBase()
c.addAttr("a", 2)
c.addAttr("a", 3)
print(c.__dict__)