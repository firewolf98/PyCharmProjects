from abc import abstractmethod


class base():
    def __init__(self, val):
        self._a = val


    @abstractmethod
    def stampa(self):
        raise NotImplementedError('action must be defined!')


class der(base):
    def __init__(self, val):
        self._b = val;


    def stampa(self):
        print(self._b)


x = der(2)
x.stampa()
