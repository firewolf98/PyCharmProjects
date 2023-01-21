#decorator factory che crea un decoratore di classe, che deve essere parametrizzato con tre cose:
#funzione che corrisponde all'esercizio di prima ad 'f'
# def decFact(classcondelegata, funz, delegata:
#   def decoratore (cls)

def decoratoreFact(Class, nomeFunz, nomeDelegata):
    def decorator(cls):
        funz = getattr(Class, nomeDelegata)
        setattr(cls, nomeFunz, funz)
        return cls
    return decorator


class ClasseConfFF:

    def ff(self):
        print("sono FF")


@decoratoreFact(ClasseConfFF, "f", "ff")
class Classe:
    def aggiungimetodo(funzione):
        if funzione is not None:
            setattr(Classe, "f", funzione)

    aggiungiMetodo = staticmethod(aggiungimetodo)


c = Classe()
c.f()

