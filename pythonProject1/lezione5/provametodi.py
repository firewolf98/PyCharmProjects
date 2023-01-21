class Methods:
    def imeth(self,x):
        print([self,x])


    def smeth(x):
        print([x])


    def cmeth(cls,x):
        print([cls,x])


    smeth=staticmethod(smeth)
    cmeth=classmethod(cmeth)


Methods.smeth(3)
obj=Methods()
obj.smeth(4)
Methods.cmeth(3)
obj.cmeth(5)