class A():
    def __init__(self, a, val):
        self._a = a
        self._val = val


    def stampa(self):
        print('a=', self._a, 'val=', self._val)


class B():
    def __init__(self, b, val):
        self._b = b
        self._val = val

    def stampa(self):
        print('b=', self._b, 'val=', self._val)


class C():
    def __init__(self, c, val):
        self._c = c
        self._val = val

    def stampa(self):
        print('c=', self._c, 'val=', self._val)


class D(A, B, C):
    def __init__(self, a, b, c, val):
        A.__init__(self, a, val)
        B.__init__(self, b, 2*val)
        C.__init__(self, c, 3*val)


    def stampa(self):
        C.stampa(self)
        B.stampa(self)
        A.stampa(self)


d = D(1, 2, 3, 123)
d.stampa()
