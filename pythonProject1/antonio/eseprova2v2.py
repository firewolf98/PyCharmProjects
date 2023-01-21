def singletonDecorator(name):
    def wrapper(cls):
        cls.counter = 0

        def __new__(cls, *args, **kwargs):
            if cls.counter < name:
                cls.counter += 1
                return object.__new__(cls, *args, **kwargs)
            else:
                raise RuntimeError

        setattr(cls, "__new__", __new__)
        return cls
    return wrapper




@singletonDecorator(2)
class C:

    def meth1(self):
        print("metodo1")

c = C()
c.meth1()
c2 = C()
c3 = C()

