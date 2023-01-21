class Creaturo:
    ISCRITTO, DUEANNO, TREANNO, DIPLOMATO = ("ISCRITTO", "SECONDO ANNO", "TERZO_ANNO", "DIPLOMATO")

    def __init__(self):
        self.succ = self.__succ
        self.pred = lambda *args : print("Non ci sono altri stati zuzzu")
        self.salta = self.__salta
        self.scuola = self.ISCRITTO

    @property
    def scuola(self):
        if self.pred != self.__pred:
            return self.ISCRITTO
        elif self.succ != self.__succ:
            return self.DIPLOMATO
        elif self.salta == self.__salta:
            return self.DUEANNO
        else:
            return  self.TREANNO

    @scuola.setter
    def scuola(self, state):
        if state == self.ISCRITTO:
            self.pred = lambda *args : print("Non ci sono altri stati zuzzu")
            self.succ = self.__succ
            self.salta = self.__salta
        elif state == self.DUEANNO:
            self.pred = self.__pred
            self.succ = self.__succ
            self.salta = self.__salta
        elif state == self.TREANNO:
            self.pred = self.__pred
            self.succ = self.__succ
            self.salta = lambda *args : print("Ma c vuo zumba, strunz")
        else:
            self.pred = self.__pred
            self.succ = lambda *args: print("Ma c vuo sturià chiù")
            self.salta = lambda *args: print("Ma c vuo zumba, strunz")

    def __succ(self):
        stato = self.scuola
        if stato == self.ISCRITTO:
            self.scuola = self.DUEANNO
        elif stato == self.DUEANNO:
            self.scuola = self.TREANNO
        else:
            self.scuola = self.DIPLOMATO

    def __pred(self):
        stato = self.scuola
        if stato == self.DIPLOMATO:
            self.scuola = self.TREANNO
        elif stato == self.TREANNO:
            self.scuola = self.DUEANNO
        else:
            self.scuola = self.ISCRITTO

    def __salta(self):
        stato = self.scuola
        if stato == self.ISCRITTO:
            self.scuola = self.TREANNO
        else:
            self.scuola = self.DIPLOMATO

    def stampastato(self):
        print("Il tuo stato è questo: ", self.scuola)


if __name__ == '__main__':
    criaturo = Creaturo()
    criaturo.stampastato()
    criaturo.succ()
    criaturo.stampastato()
    criaturo.succ()
    criaturo.stampastato()
    criaturo.succ()
    criaturo.stampastato()
    criaturo.pred()
    criaturo.stampastato()
    criaturo.pred()
    criaturo.stampastato()
    criaturo.pred()
    criaturo.stampastato()
    criaturo.salta()
    criaturo.stampastato()
    criaturo.salta()
    criaturo.stampastato()
