def dec(function):
    def wrapper(*args, **kwargs):
        print("dec di we")
        return function(*args, **kwargs)
    return wrapper


def deccls(name):
    def wrapper(cls):
        f = getattr(cls, name)

        def newf(self):
            print("sono f aggiornata")
            return f(self)
        setattr(cls, name, newf)
        return cls
    return wrapper


@deccls("printwe")
class C:
    def __init__(self):
        self.we = "ciao"

    @dec
    def printwe(self):
        print(self.we)
        print("aaa")

        return self.we


c = C()
print(c.printwe())