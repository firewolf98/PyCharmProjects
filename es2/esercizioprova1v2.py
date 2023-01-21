class Pacco:
    ORDINATO, SPEDITO, RICEVUTO = ("ORDINATO", "SPEDITO", "RICEVUTO")

    def __init__(self):
        self.next = self.__succ
        self.prev = lambda *args: print("Non è possibile tornare indietro")
        self.stato = Pacco.ORDINATO

    @property
    def stato(self):
        if self.prev != self.__prev:
            return Pacco.ORDINATO
        elif self.prev == self.__prev and self.next == self.__succ:
            return Pacco.SPEDITO
        else:
            return Pacco.RICEVUTO

    @stato.setter
    def stato(self, state):
        if state == Pacco.ORDINATO:
            self.next = self.__succ
            self.prev = lambda *args: print("Non è possibile tornare indietro")
        elif state == Pacco.SPEDITO:
            self.next = self.__succ
            self.prev = self.__prev
        elif state == Pacco.RICEVUTO:
            self.next = lambda *args: print("Il pacco e`già stato ricevuto ")
            self.prev = self.__prev

    def __succ(self):
            if self.stato == Pacco.ORDINATO:
                self.stato = Pacco.SPEDITO
            else:
                self.stato = Pacco.RICEVUTO

    def __prev(self):
        if self.stato == Pacco.RICEVUTO:
            self.stato = Pacco.SPEDITO
        else:
            self.stato = Pacco.ORDINATO

    def stampaStato(self):
        if self.stato == Pacco.ORDINATO:
            print("Il pacco e` stato ordinato ma non ancora spedito")
        elif self.stato == Pacco.SPEDITO:
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
