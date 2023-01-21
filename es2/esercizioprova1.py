class Pacco:
    ORDINATO, SPEDITO, RICEVUTO = ("ORDINATO", "SPEDITO", "RICEVUTO")

    def __init__(self):
        #self.stato = self.ORDINATO
        self.next = self.__succSpedito
        self.stato = Pacco.ORDINATO

    @property
    def stato(self):
        if self.next == Pacco.__succSpedito:
            return Pacco.ORDINATO
        elif self.next == Pacco.__succRicevuto:
            return Pacco.SPEDITO
        else:
            return Pacco.RICEVUTO

    @stato.setter
    def stato(self, state):
        if state == Pacco.SPEDITO:
            self.next = self.__succRicevuto
        elif state == Pacco.RICEVUTO:
            self.next = lambda *args: print("Il pacco e`già stato ricevuto ")

    def __succSpedito(self):
            self.stato = Pacco.SPEDITO

    def __succRicevuto(self):
            self.stato = Pacco.RICEVUTO

    def stampaStato(self):
        statoAttuale = self.stato
        if statoAttuale == Pacco.ORDINATO:
            print("Il pacco e` stato ordinato ma non ancora spedito")
        elif statoAttuale == Pacco.SPEDITO:
            print("Il pacco e` stato spedito ma non ancora ricevuto")
        else:
            print("Il pacco e` stato ricevuto ")



def main():
    print("\nCreo il pacco")
    pacco = Pacco()
    pacco.stampaStato()
    print("\nInoltro il pacco all'ufficio postale")
    pacco.next()
    pacco.stampaStato()
    print("\nConsegno il pacco al destinatario")
    pacco.next()
    pacco.stampaStato()
    print("\nProvo a passare ad uno stato successivo")
    pacco.next()
    pacco.stampaStato()

if __name__== "__main__":
    main()


"""Il  programma deve stampare:
Creo il pacco
Il pacco e` stato ordinato ma non ancora spedito

Inoltro il pacco all'ufficio postale
Il pacco e` stato spedito ma non ancora ricevuto

Consegno il pacco al destinatario
Il pacco e` stato ricevuto 

Provo a passare ad uno stato successivo
Il pacco e` gia` stato ricevuto
Il pacco e` stato ricevuto 
"""
