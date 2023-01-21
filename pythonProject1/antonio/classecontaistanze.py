from functools import wraps

def contatore(cls):
    @wraps(cls)
    def wrapper():
        cls.nIstanze += 1
        return cls
    return wrapper


@contatore
class C:
    nIstanze = 0

    def met1(self):
        print("we")


c = C()
c2 = C()
c3 = C()
print(c.nIstanze)
print(C.__name__)
