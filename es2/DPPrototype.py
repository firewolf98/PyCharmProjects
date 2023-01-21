import copy
import sys


class classePrototipo:
    def __init__(self, valore1, valore2):
        self.v1 = valore1
        self.v2 = valore2

    def setValori(self, val1, val2):
        self.v1 = val1
        self.v2 = val2


def make_object(Class, *args, **kwargs):
    return Class(*args, **kwargs)


if __name__ == '__main__':
    c1 = classePrototipo(5, 10)
    c2 = copy.deepcopy(c1)
    c2.setValori(1, 2)
    c3 = c1.__class__(8, 9)
    c4 = globals()["classePrototipo"](4, 5)
    c5 = getattr(sys.modules[__name__], "classePrototipo")(10, 11)
    c6 = eval("{}({}, {})".format("classePrototipo", 12, 13))
    c7 = make_object(classePrototipo, 13, 14)