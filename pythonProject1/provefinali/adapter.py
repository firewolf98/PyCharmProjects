from provefinali.utility import Commesso, Cuoco, Musicista

class Adapter:
    def __init__(self, obj):
        self.obj = obj


    def __str__(self):
        return str(self.obj)


    def lavora(self,qualcosa):
        if isinstance(self.obj, Commesso):
            return self.obj.vende(qualcosa)
        if isinstance(self.obj, Musicista):
            return self.obj.suona(qualcosa)
        if isinstance(self.obj, Cuoco):
            return self.obj.cucina(qualcosa)


if __name__ == '__main__':
    c = Cuoco("Antonio")
    m = Musicista("Veronica")
    z = Commesso("Luca")
    adapt = Adapter(c)
    print(adapt, adapt.lavora("la lasagna"))
