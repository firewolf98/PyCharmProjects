class State_d:
    def __init__(self, imp):
        self.__implementation=imp
    def changeImp(self, newImp):
        self.__implementation=newImp
    def __getattr__(self, item):
        return getattr(self.__implementation,item)


class Implem1:
    def f(self):
        print('f imp1')
    def g(self):
        print('g imp1')
    def h(self):
        print('h imp1')


class Implem2:
    def f(self):
        print('f imp2')
    def g(self):
        print('g imp2')
    def h(self):
        print('h imp2')


def run(b):
    b.f()
    b.g()
    b.h()
    b.g()


b = State_d(Implem1())
run(b)
b.changeImp(Implem2())
run(b)