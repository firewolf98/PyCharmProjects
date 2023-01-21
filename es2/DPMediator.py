import collections
class mediator():
    def __init__(self, listaOggetti):
        self.callable = collections.defaultdict(list)
        classe, metodo = listaOggetti
        self.callable[classe].append(metodo);
        classe.mediator = self

    def onMediate(self, classe):
        callables = self.callable.get(classe)
        if callables is not None:
            for call in callables:
                call(classe)


class mediated():
    def __init__(self):
        self.mediator = None

    def onMediate(self):
        if self.mediator is not None:
            self.mediator.onMediate(self)

class banca:
    def __init__(self):

        self.banckaccount = bancaccount()
        self.mediator = mediator(((self.banckaccount, self.showSaldo)))


    def showSaldo(self, classe):
        print(classe.saldo)


class bancaccount(mediated):

    def __init__(self):
        super().__init__()
        self.saldo = 1000

    def addSaldo(self, importo):
        self.saldo += importo
        self.onMediate()

banca = banca()
banca.banckaccount.addSaldo(500)

