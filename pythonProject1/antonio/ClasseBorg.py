class Borg:
    shared_state = {}
    def __new__(cls, *args, **kwargs):
        obj = super(Borg, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.shared_state
        return obj

class C(Borg):
    shared_state = {}


b = Borg()
b.we = "ciao"
print(b.we)
c = C()
print(c.we)