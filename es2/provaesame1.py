#Scrivere la funzione conta all’interno del file esercizio4.py. Se la funzione ha bisogno di
#invocare altre procedure, fornire anche quest’ultime. La funzione conta prende in input
#una stringa parola, una lista di nomi di file listaFile e il parametro concorrenza. Facendo
#uso di Futures e Multiprocessing, la funzione conta deve contare quante volte parola
#appare in ciascuno dei file di listaFile e stampare per ciascun file l’intero computato. Cio`
#deve essere fatto con un processo separato per ogni file di listaFile e le stampe devono
#essere effettuate nell’ordine in cui terminano i processi. Il callable usato da conta deve
#prendere in input la lista di file e la parola.

from concurrent import futures
import re


def worker(word, file, *args):
    regex = re.compile(r"\w+")
    total = 0
    with open(file) as file:
        for line in file:
            for match in regex.findall(line):
                if match == word:
                    total+=1

    return total


def wait_for_end(futuresPool):
    for future in futures.as_completed(futuresPool):
        print(future.result())


def conta(word, list_file, concurrency):
    futuresPool = set()
    with futures.ProcessPoolExecutor(max_workers = concurrency) as Executor:
        for file in list_file:
            future = Executor.submit(worker, word, file)
            futuresPool.add(future)
    wait_for_end(futuresPool)


if __name__ == '__main__':
    concurrency = 4
    word = "ciao"
    list_file = ["./wewe.txt", "./wewe2.txt"]
    conta(word, list_file, concurrency)