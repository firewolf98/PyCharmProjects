class C:
    numIstances = 0

    def __init__(self):
        C.numIstances += 1

    def contaIstanze(cls):
        return cls.numIstances

    contaIstanze = classmethod(contaIstanze)

class D(C):
    numIstances = 0

    def __init__(self):
        D.numIstances +=1


c1 = C()
c = C()
d = D()

d = D()
d = D()

print(C.contaIstanze())
print(D.contaIstanze())