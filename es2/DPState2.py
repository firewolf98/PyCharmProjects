from random import randint
class interruttore():
    ON, OFF = ("ON", "OFF")

    def __init__(self):
        self.funzione = self.__funzione
        self.counter = 0

    @property
    def stateprop(self):
        return (interruttore.ON if self.funzione == self.__funzione
                else interruttore.OFF)

    @stateprop.setter
    def stateprop(self, state):
        if state == interruttore.ON:
            self.funzione = self.__funzione
        else:
            self.funzione = lambda *args: None

    def __funzione(self):
            print("Sto facendo la funzione")
            self.counter += 1

    def counters(self):
        return self.counter


if __name__ == '__main__':
    inter = interruttore()

    for _ in range(100):
        i = randint(0, 10)
        if i < 3:
            inter.stateprop = "OFF"
        else:
            inter.stateprop = "ON"
        print(inter.stateprop)
        inter.funzione()

    print(inter.counters())
