def count(aClass):
    aClass.numInstances = 0
    return aClass


@count
def Spam():
    pass


@count
class Other():
    pass


Spam.numInstances
Other.numInstances
