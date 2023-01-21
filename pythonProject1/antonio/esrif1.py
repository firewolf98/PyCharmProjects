#decoratore di classe che conta le istanze
from functools import wraps
def decorator(cls):
    class newC(cls):
        def __init__(self):
            cls.numIstanze+=1
        cls.numIstanze = 0
        def getIstances():
            return cls.numIstanze
        getIstances = staticmethod(getIstances)
    return newC


@decorator
class C:
    def met1(self):pass
    def met2(self):pass


c = C()
print(c.getIstances())
