import itertools

class observer:
    def __init__(self):
        self.__osservatore = set()

    def add_osservatore(self, influenzato, *influenzati):
        for influenzat in itertools.chain((influenzato,), influenzati):
            self.__osservatore.add(influenzat)
            #influenzat.aggiorna(self)

    def del_osservatore(self, influenzato):
        self.__osservatore.discard(influenzato)

    def notifica_influenzati(self):
        for influenzato in self.__osservatore:
            influenzato.aggiorna(self)


class osservata(observer):
    def __init__(self, importo):
        super().__init__()
        self.soldi = importo

    @property
    def soldini(self):
        return self.soldi

    @soldini.setter
    def soldini(self, amount):
        self.soldi += amount
        self.notifica_influenzati()


class influenzata:

    def __init__(self): pass

    def aggiorna(self, osservato):
        print("Sono stati aggiunti soldi al conto, ora ci sono: ", osservato.soldini)


if __name__ == '__main__':
    inf = influenzata()
    oss = osservata(1000)
    oss.add_osservatore(inf)
    oss.soldini = 500
