class Prod:
    def __init__(self, value):
        self.value = value
    def __call__(self, other):
        return self.value*other


x = Prod(4)
print(x(4))
