from antonio.utility import Commesso, Cuoco, Musicista

class Adapter:
    def __init__(self, obj, adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __str__(self):
        return str(self.obj)


class Lavoratore:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return "il lavoratore {}".format(self.nome)

    def lavora(self, lavoro):
        return "svolge il seguente {}".format(lavoro)


if __name__ == '__main__':
    l = Lavoratore("Gianmarco")
    l.lavora("zappatore")

    c = Cuoco("Antonio")
    #passando l'adapter ad una nuova variabile
    z = Adapter(c, dict(lavora=c.cucina))
    #se si invoca il metodo bisogna passare self
    comm = Adapter(Commesso("Paolo"), dict(lavora=Commesso.vende))
    m = Musicista("Veronica")
    m = Adapter(m, dict(lavora=m.suona))

    #print(z.__dict__)
    #print(z)
    #print(z.lavora("lasagna"))
    #print(comm.lavora(comm,"abiti"))
    #m.lavora("musica pop")
    print("{} {}".format(comm, comm.lavora(comm, "abiti")))
    print("{} {}".format(m, m.lavora("musica pop")))
    print("{} {}".format(z, z.lavora("una lasagna")))
