class Spam:
    numInstances = 0

    def __init__(self):
        Spam.numInstances += 1

    def printNumInstances(cls):
        print('Num instances %s' % cls.numInstances)
    printNumInstances = classmethod(printNumInstances)


class Sub(Spam):
    def printNumInstances(cls):
        print('Extra', cls)
        Spam.printNumInstances()
    printNumInstances = classmethod(printNumInstances)


class Other(Spam):
    pass


a = Spam()
b = Spam()
a.printNumInstances()
Spam.printNumInstances()


x = Sub()
y = Spam()
x.printNumInstances()
Sub.printNumInstances()
y.printNumInstances()
z = Other()
z.printNumInstances()
