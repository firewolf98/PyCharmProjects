class AbstractClass:

    def metodo1(self):
        raise NotImplementedError("Lo facciamo questo metodo1?")

    def metodo2(self):
        raise NotImplementedError("Lo facciamo questo metodo2?")

class Implementatore1(AbstractClass):

    def metodo1(self):
        print("Sono metodo1 implementato dalla classe implementatore1")

    def metodo2(self):
        print("Sono metodo2 implementato dalla classe implementatore1")


class Implementatore2(AbstractClass):

    def metodo1(self):
        print("Sono metodo1 implementato dalla classe implementatore2")

    def metodo2(self):
        print("Sono metodo2 implementato dalla classe implementatore2")


if __name__ == '__main__':
    c1 = Implementatore1()

    c1.metodo1()
    c1.metodo2()

    c2 = Implementatore2()

    c2.metodo1()
    c2.metodo2()

    c3 = AbstractClass()

    try:
        c3.metodo1()
    except: pass

    try:
        c3.metodo2()
    except: pass

    c3.metodo1()