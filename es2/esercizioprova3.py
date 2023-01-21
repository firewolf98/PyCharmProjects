class FW():
    """
    FW memorizza la parte comune dello stato in SharedState

    """

    def __init__(self, sharedState: list):
        self.shared_state = sharedState

    """op aggiunge un oggetto oggetto al file  prendendo tutta la parte condivisa dell'auto da sharedState e il resto dal
    parametro itsOwnState"""

    def op(self, itsOwnState: list, tipo: type, file):

        print("Il nuovo oggetto di tipo", tipo, "e\' ", self.shared_state+itsOwnState)
        return tipo(self.shared_state+itsOwnState)


class FWFactory():
    """
    Questa classe crea oggetti FW: ne crea uno nuovo se non esiste, altrimenti resituisce uno preesistente

    """
    def __init__(self, sharedState):
        self.sharedd_state = sharedState

    def get_FW(self, shared_state: list) -> FW:
        """
        restituisce un FW con un certo stato o ne crea uno nuovo
        """
        if shared_state in self.sharedd_state:
            print("FWFactory: Uso un FW esistente")
            return FW(shared_state)
        else:
            print("FWFactory: Non trovo FW ne creo uno nuovo")
            self.sharedd_state.append(shared_state)
            return FW(shared_state)

    def list_FWs(self):
        """ stampa numero oggetti FW's e gli stati degli FW's"""
        print("Numero: ", len(self.sharedd_state))
        for marca, modello, colore in self.sharedd_state:
            print(modello,"_", marca, "_", colore)


class automobile:
    def __init__(self, state: list):
        self._state = state

    def state(self): return self._state


def add_car(factory: FWFactory, targa: str, proprietario: str, marca: str, modello: str, colore: str):
    print("\n\nClient: Aggiungo un automobile.")
    fw = factory.get_FW([marca, modello, colore])

    fw.op([targa, proprietario], automobile, "automobili.txt")


if __name__ == "__main__":
    """
    The client code usually creates a bunch of pre-populated flyweights in the
    initialization stage of the application.
    """

    factory = FWFactory([
        ["Chevrolet", "Camaro2018", "rosa"],
        ["Mercedes Benz", "C300", "nera"],
        ["Mercedes Benz", "C500", "rossa"],
        ["BMW", "M5", "rossa"],
        ["BMW", "X6", "bianca"],
    ])

    factory.list_FWs()

    add_car(
        factory, "DE123AT", "Bob Bab", "BMW", "M5", "rossa")

    add_car(
        factory, "AR324SD", "Mike Smith", "BMW", "X1", "rossa")

    print("\n")

    factory.list_FWs()

"""Il programma stampa :

FWFactory: ho  5 oggetti FW: 
Camaro2018_Chevrolet_rosa
C300_Mercedes Benz_nera
C500_Mercedes Benz_rossa
BMW_M5_rossa
BMW_X6_bianca


Client: Aggiungo un automobile.
FWFactory:  uso un FW esistente.
Il nuovo oggetto di tipo <class '__main__.automobile'> e` ['BMW', 'M5', 'rossa', 'DE123AT', 'Bob Bab']:


Client: Aggiungo un automobile.
FWFactory: non trovo un FW, ne creo uno nuovo.
Il nuovo oggetto di tipo <class '__main__.automobile'> e` ['BMW', 'X1', 'rossa', 'AR324SD', 'Mike Smith']:


FWFactory: ho  6 oggetti FW: 
Camaro2018_Chevrolet_rosa
C300_Mercedes Benz_nera
C500_Mercedes Benz_rossa
BMW_M5_rossa
BMW_X6_bianca
BMW_X1_rossa

"""
