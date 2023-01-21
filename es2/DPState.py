from random import randint
class interruttore():
    def __init__(self):
        self.state = True
        self.counter = 0


    def pulsanteOnOff(self):
        if self.state:
            self.state = False
            return self.state
        else:
            self.state = True

    def funzione(self):
        if self.state:
            print("Sto facendo la funzione")
            self.counter += 1
        else:
            print("-------")
    def counters(self):
        return self.counter


if __name__ == '__main__':
    inter = interruttore()

    for _ in range(100):
        i = randint(0,10)
        if i < 5:
            inter.pulsanteOnOff()
        inter.funzione()

    print(inter.counters())
