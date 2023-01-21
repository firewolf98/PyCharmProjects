def contatore(function):
    def wrapper(*args):
        args[0].nIstanze += 1
        function(args[0])
    return wrapper

class C():
    def __init__(self):
        self.nIstanze = 0

    @contatore
    def meth1(self): print("we")

    def meth2(self): pass
    def getIstanze(self):
        return self.nIstanze


c = C()
print(c.getIstanze())
c.meth1()
print(c.getIstanze())
