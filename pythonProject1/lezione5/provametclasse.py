class Spam:
    numInstances=0
    def __init__(self):
        Spam.numInstances+=1
    def printNumInstances(cls):
        print("NumInstances %s" % cls.numInstances)
    printNumInstances=classmethod(printNumInstances)

class Sub(Spam):
    def printNumInstances(cls):
        print("Extra stuff...", cls)
        Spam.printNumInstances()
    printNumInstances = classmethod(printNumInstances)

class Other(Spam):
    pass


print("---------")
x,y=Sub(),Spam()
x.printNumInstances()
Sub.printNumInstances()
y.printNumInstances()
z=Other()
z.printNumInstances()