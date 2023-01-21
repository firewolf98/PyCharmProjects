class Spam:
    numInstances = 0

    def __init__(self):
        Spam.numInstances += 1

    def printNumInstances():
        print('Num instances %s' % Spam.numInstances)
    printNumInstances = staticmethod(printNumInstances)


class Sub(Spam):
    def printNumInstances():
        print('Extra')
        Spam.printNumInstances()
    printNumInstances = staticmethod(printNumInstances)


a = Spam()
b = Spam()
c = Spam()
Spam.printNumInstances()
a.printNumInstances()


c = Sub()
d = Sub()
c.printNumInstances()
Sub.printNumInstances()
Spam.printNumInstances()
