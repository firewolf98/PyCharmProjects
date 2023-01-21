def singletonDecorator(cls):
    class newCls(cls):
        cls.istanza = None

        def __new__(cls, *args, **kwargs):
            print("we")
            if cls.istanza is None:
                print("wewe")
                cls.istanza = object.__new__(cls)
                return cls.istanza
            else:
                raise RuntimeError

    return newCls




@singletonDecorator
class C:

    def meth1(self):
        print("metodo1")


c = C()
c.meth1()

