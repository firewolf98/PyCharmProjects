class C:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        print("au")
        ''' Proprietà'''
        return self._x

    @x.setter
    def x(self, x):
        print("wewe")
        self._x = x

    @x.deleter
    def x(self):
        del self._x

c = C()
c.x= 4
del c.x
print(c.x)