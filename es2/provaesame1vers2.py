#Scrivere la funzione conta all’interno del file esercizio4.py. Se la funzione ha bisogno di
#invocare altre procedure, fornire anche quest’ultime. La funzione conta prende in input
#una stringa parola, una lista di nomi di file listaFile e il parametro concorrenza. Facendo
#uso di Futures e Multiprocessing, la funzione conta deve contare quante volte parola
#appare in ciascuno dei file di listaFile e stampare per ciascun file l’intero computato. Cio`
#deve essere fatto con un processo separato per ogni file di listaFile e le stampe devono
#essere effettuate nell’ordine in cui terminano i processi. Il callable usato da conta deve
#prendere in input la lista di file e la parola.
from concurrent import futures


def get_jobs(files, stringhe):

    for stringa, file in zip(stringhe, files):
        with open(file, "r") as file:
            f = file.read()
        yield stringa, f


def worker(stringa, contenuto):
    conta = 0
    for l in contenuto.split():
        if l == stringa:
            conta +=1
    if conta == 0:
        return (False, conta)
    else:
        return (True, conta)


def wait_for_end(futuresPool, stringhe, files):
    for flag, future in enumerate(futures.as_completed(futuresPool)):
        pos = 0
        print(flag, "  ", future.result())
        if future.result() == True:
            print("La stringa {} è presente {} volte nel file {}".format(stringhe[pos], future.result(), files[pos]))
        elif future.result() == False:
            print("La stringa {} non è presente nel file {}".format(stringhe[pos], files[pos]))


def procTesto(files, stringhe, concurrency):
    futuresPool = set()
    with futures.ProcessPoolExecutor(max_workers=concurrency) as Executor:
        for stringa, contenuto in get_jobs(files, stringhe):
            future = Executor.submit(worker, stringa, contenuto)
            futuresPool.add(future)
    wait_for_end(futuresPool, stringhe, files)




if __name__ == '__main__':
    files = ["wewe.txt", "wewe2.txt", "wewe3.txt", "wewe.txt", "wewe2.txt", "wewe3.txt"]
    stringhe = ["panca", "Trento", "entrarono", "a", "di", "capra"]

    procTesto(files, stringhe, 6)

