class C:
    __slots_ = ["nome", "cognome", "eta"]
    #_shared_state = {"nome":"", "cognome":"", "eta": 0}


    def __new__(cls, *args, **kwargs):
        obj = super(C, cls).__new__(cls, *args, **kwargs)
        obj.__slots__= cls.__slots_
        return obj


    def __init__(self): pass


c = C()
c.nome = "www"
c.cognome = "aaa"
c.eta = 17
print(c.nome, c.cognome, c.eta)
c2 = C()
print(c2.eta)