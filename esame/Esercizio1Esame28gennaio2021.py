"""Scrivere nel file esercizio1.py una funzione che prende in input una sequenza di richieste
(stringhe) e passa ciascuna richiesta ad una catena di gestori ciascuno dei quali e‘ una
coroutine (usando il decoratore @coroutine visto a lezione).
• Se la stringa comincia con una lettera compresa tra ‘a’ e ‘g’ allora la richiesta viene
gestita dal gestore gestore_ag che stampa “Richiesta {} gestita da gestore_ag’’.
• Se la stringa comincia con una lettera compresa tra ‘h’ e ‘n’ allora la richiesta viene
gestita dal gestore gestore_hn che stampa “Richiesta {} gestita da gestore_hn’’.
• Se la stringa NON comincia con una lettera allora la richiesta viene gestita dal
gestore gestore_distr che stampa “Richiesta {} gestita da gestore_distr: uso
improprio della catena di gestori’’ e poi smette di funzionare.
• Se la stringa comincia con una lettera dell’alfabeto successiva ad ‘n’ o con una
maiuscola allora la richiesta viene gestita dal gestore gestoreDiDefault che stampa
“Messaggio da gestoreDiDefault: non è stato possibile gestire la richiesta {} “.
Nelle suddette stampe il nome della richiesta deve comparire al posto delle parentesi
graffe.
Se ad un certo punto un gestore manda la richiesta al suo successore e il successore
smette di funzionare allora anche il gestore che inviato la richiesta deve smettere di
funzionare. Prima di smettere di funzionare il gestore deve stampare “Il successore
di {} ha smesso di funzionare a causa della richiesta {} e di conseguenza smette di
funzionare anche {}’’, dove al posto della I e III coppia di parentesi graffe deve
comparire il nome del gestore e al posto della II coppia il nome della richiesta."""
import functools


def coroutine(function):
    @functools.wraps(function)
    def wrapper(*args ,**kwargs):
        generator = function(*args, **kwargs)
        next(generator)
        return generator
    return wrapper

def smistamento( richiesta):
    pipeline = gestore_distr(gestore_ag(gestore_hn(gestoreDiDefault())))
    pipeline.send(richiesta)
    #oppure:
    #gestore_distr(gestore_ag(gestore_hn(gestoreDiDefault()))).send(richiesta)


@coroutine
def gestore_distr(successor):
    while True:
        try:
            richiesta = (yield)
            #richiesta = str(richiesta)
            #if (str(richiesta[0]) <"a" or str(richiesta[0])> "z") and isinstance(richiesta[0], int):
            if richiesta[0].isdigit():
                print("Richiesta {} gestita da gestore_distr".format(richiesta))
            elif successor is not None:
                successor.send(richiesta)
        except StopIteration:
            print(
                "Il successore di {0} ha smesso di funzionare a causa della richiesta {1} e di conseguenza smette di funzionare anche {0}".format(
                    "gestore_distr", richiesta))


@coroutine
def gestore_ag(successor):
    while True:
        try:
            richiesta = (yield)
            if richiesta[0] >="a" and richiesta[0]<= "g":
                print("Richiesta {} gestita da gestore_ag".format(richiesta))
                #break
            elif successor is not None:
                successor.send(richiesta)
        except StopIteration:
            print("Il successore di {0} ha smesso di funzionare a causa della richiesta {1} e di conseguenza smette di funzionare anche {0}".format(
                    "gestore_ag", richiesta))


@coroutine
def gestore_hn(successor):
    while True:
        try:
            richiesta = (yield)
            if richiesta[0] >="h" and richiesta[0]<= "n":
                print("Richiesta {} gestita da gestore_hn".format(richiesta))
                #break
            elif successor is not None:
                successor.send(richiesta)
        except StopIteration:
            print("Il successore di {0} ha smesso di funzionare a causa della richiesta {1} e di conseguenza smette di funzionare anche {0}".format("gestore_hn",richiesta))


@coroutine
def gestoreDiDefault():
    while True:
        richiesta = (yield )
        if richiesta[0] > 'n' or (richiesta[0] >="A" and richiesta[0] <= "Z"):
            print("Richiesta {} gestita da gestoreDiDefault".format(richiesta))
        else:
            print("Messaggio da gestoreDiDefault: non è stato possibile gestire la richiesta {}".format(richiesta))
            break


if __name__ == "__main__":
    smistamento("albero")
    smistamento("nuvola")
    smistamento("1prova")
    smistamento("Casa")
    smistamento("!cosa?!")