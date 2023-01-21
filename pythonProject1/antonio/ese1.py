def decoratore(Class):
        if "ff" not in dir(Class):
            setattr(Class, "ff", ClasseConfFF.ff)
        return Class


class ClasseConfFF:

    def ff(self):
        print("sono FF")

@decoratore
class Classe:
    def aggiungimetodo(funzione):
        if funzione is not None:
            setattr(Classe, "f", funzione)
    aggiungiMetodo = staticmethod(aggiungimetodo)


c = Classe()
print(c.ff())

