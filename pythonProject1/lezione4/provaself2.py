class provaself2():
    common=[]

    def __init__(self,*args):
        self.L=[]
        for val in args:
            self.L.append(val)
            self.common.append(val)

    def __str__(self):
        return str(self.L)

    def out(self):
        for val in self.common:
            print(val,end="")
        print()

a=provaself2()
b=provaself2(3,4)
c=provaself2(5,6)
print(a)
print(b)
print(c)
a.out()
b.out()
c.out()