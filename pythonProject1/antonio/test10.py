# scrivere un decoratore di classe che dato un metodo ne aggiunge una funzione di validazione
def decoratorCheck(name):
    def wrapper(cls):
        if name.__contains__("Str"):
            setattr(cls, "old", getattr(cls, name))
            def newMeth(self, *args, **kwargs):
                if isinstance(args[0], str):
                    getattr(cls, "old")(self, *args, **kwargs)
                else:
                    raise ValueError("Valore inserito non corretto")
            setattr(cls, name, newMeth)
        elif name.__contains__("Int"):
            setattr(cls, "old", getattr(cls, name))

            def newMeth(self, *args, **kwargs):
                if isinstance(args[0], int):
                    getattr(cls, "old")(self, *args, **kwargs)
                else:
                    raise ValueError("Valore inserito non corretto")
            setattr(cls, name, newMeth)
        return cls
    return wrapper


@decoratorCheck("methInt")
class C:

    def methStr(self, str):
        print("Ecco la stringa: " + str)

    def methInt(self, inte):
        print(inte + inte)

c = C()
c.methInt("aaa")