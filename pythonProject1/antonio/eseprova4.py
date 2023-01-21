def contaIstanze(cls):
    def __new__(cls):
        cls.contatore = 0
        if cls.__bases__[0] != object.__mro__[0]:
            cls.__bases__[0].contatore += 1
        return object.__new__(cls)

    def contaIstanze(cls):
        return cls.contatore
    contaIstanze = classmethod(contaIstanze)
    setattr(cls, "contaIstanze", contaIstanze)
    setattr(cls, "__new__", __new__)
    return cls

@contaIstanze
class C: pass


class C2(C): pass


class C3(C2): pass


c = C()
print(c.contaIstanze())
c2 = C2()
c3 = C3()
c3 = C3()
cc3 = C3()


print(C2.__dict__)
print(C.contaIstanze())