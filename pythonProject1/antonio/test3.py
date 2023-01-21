l = [1, 2, 3, 4]


class C:
    def __init__(self, *args):
        self.l = args

    def m1(self): pass

    def __call__(self, *args, **kwargs):
        print("mammt")

    #def __iter__(self):
    #    for x in self.l:
    #       yield x

    def __len__(self):
        return len(self.l)

    def __getitem__(self, item):
        return self.l[item]

    def astratto(self):
        raise NotImplementedError("implementami strunz")

class A(C):

    def astratto(self):
        print("ho fatto bastard")



print(l)
print(*l)
c = C(1,2,3,4,5)
print(c.l)

for x in c:
    print(x)

if 50 in c:
    print("c'è")

print(C.__mro__)

it = iter(l)
try:
    while next(x for x in it):
        print(x)
except StopIteration as e:
    print(e)


c.astratto()
a = A()
a.astratto()
