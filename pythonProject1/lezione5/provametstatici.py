class Spam:
    numInstances=0
    def __init__(self):
        Spam.numInstances=Spam.numInstances+1
    def printNumInstances():
        print("NumInstances %s" % Spam.numInstances)
    printNumInstances=staticmethod(printNumInstances)

class Sub(Spam):
    def printNumInstances():
        print("Extra stuff...")
        Spam.printNumInstances()
    printNumInstances = staticmethod(printNumInstances)


a=Spam()
b=Spam()
c=Spam()
Spam.printNumInstances()
a.printNumInstances()
print("----------------------")
c=Sub()
d=Sub()
c.printNumInstances()
Sub.printNumInstances()
Spam.printNumInstances()