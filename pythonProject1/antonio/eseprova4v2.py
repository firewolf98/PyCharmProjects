def contaIstanze(cls):
    cls.contatore = 0

    def __init__(self):
        self.contatore = 0
        if self.__class__.__bases__[0] != object.__mro__[0]:
            self.__class__.__bases__[0].contatore += 1

    def contaIstanze():
        return cls.contatore

    contaIstanze = staticmethod(contaIstanze)
    setattr(cls, "contaIstanze", contaIstanze)
    setattr(cls, "__init__", __init__)
    return cls


@contaIstanze
class C: pass


class C2(C): pass


class C3(C): pass


c = C()
print(c.contaIstanze())
c2 = C2()
print(c2.contaIstanze())
