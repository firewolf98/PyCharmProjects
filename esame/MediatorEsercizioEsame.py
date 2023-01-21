import datetime


# completare la classe Casa (completare  __init__ e aggiungere i metodi necessari)
from MediatorEsercizioEsameMod import *


class Casa:

    def __init__(self, nomePadrone, nomeCane1, nomeCane2, oraUltimaPappa1, oraUltimaPappa2):
        self.allerta = False
        self.padrone = Persona(nomePadrone)
        self.cane1 = Cane(nomeCane1, oraUltimaPappa1)
        self.cane2 = Cane(nomeCane2, oraUltimaPappa2)
        self.mediator = self.creaMediator()

    def creaMediator(self):
        return Mediator(((self.padrone, self.daiPappa), (self.cane1, self.allertaPadrone), (self.cane2, self.allertaPadrone)))

    def allertaPadrone(self, cane):
        self.allerta = True
        print("il cane {} abbaia".format(cane.nome))

    def daiPappa(self, padrone):
        if self.allerta:
            if (padrone.ora_ritorno - self.cane1.oraUltimaPappa).total_seconds() / 60 / 60 > 4:
                self.cane1.oraUltimaPappa = padrone.ora_ritorno
                print("Il padrone da` la pappa al cane {} ".format(self.cane1.nome))

            if (padrone.ora_ritorno - self.cane2.oraUltimaPappa).total_seconds() / 60 / 60 > 4:
                self.cane2.oraUltimaPappa = padrone.ora_ritorno
                print("Il padrone da` la pappa al cane {} ".format(self.cane2.nome))

            self.allerta = False


def main():
    casa = Casa("Maria", "Bob", "Ted", datetime.datetime(year=2020, month=1, day=11, hour=10),
                datetime.datetime(year=2020, month=1, day=11, hour=11))
    print("Il cane {} ha mangiato alle {} per l'ultima volta".format(casa.cane1.nome,
                                                                     (casa.cane1.oraUltimaPappa.strftime('%H:%M'))))
    print("Il cane {} ha mangiato alle {} per l'ultima volta".format(casa.cane2.nome,
                                                                     (casa.cane2.oraUltimaPappa.strftime('%H:%M'))))

    casa.padrone.esce()
    casa.cane1.abbaia()
    casa.padrone.torna_a_casa(datetime.datetime(year=2020, month=1, day=11, hour=15))
    casa.padrone.esce()
    casa.cane2.abbaia()
    casa.padrone.torna_a_casa(datetime.datetime(year=2020, month=1, day=11, hour=17))
    casa.padrone.esce()
    casa.padrone.torna_a_casa(datetime.datetime(year=2020, month=1, day=11, hour=18))
    casa.padrone.esce()
    casa.cane1.abbaia()
    casa.padrone.torna_a_casa(datetime.datetime(year=2020, month=1, day=11, hour=23))


if __name__ == "__main__": main()

"""
Il programma deve stampare:
Il cane Bob ha mangiato alle 10:00 per l'ultima volta
Il cane Ted ha mangiato alle 11:00 per l'ultima volta
Il padrone dei cani esce di casa
Il cane Bob abbaia
Il padrone dei cani torna a casa alle 15:00
Il padrone da` la pappa al cane  Bob
Il padrone dei cani esce di casa
Il cane Ted abbaia
Il padrone dei cani torna a casa alle 17:00
Il padrone da` la pappa al cane  Ted
Il padrone dei cani esce di casa
Il padrone dei cani torna a casa alle 18:00
Il padrone dei cani esce di casa
Il cane Bob abbaia
Il padrone dei cani torna a casa alle 23:00
Il padrone da` la pappa al cane  Bob
Il padrone da` la pappa al cane  Ted


"""
