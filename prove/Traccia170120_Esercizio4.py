"""Scrivere la funzione cerca all’interno del file esercizio4.py. Se la funzione ha bisogno di
invocare altre procedure, fornire anche quest’ultime. La funzione cerca prende in input
una lista di stringhe listaParole e una lista di nomi di file listaDiFile, e il parametro
concorrenza. Facendo uso di multiprocessing.JoinableQueue, la funzione cerca deve
stampare per ciascuno dei file di listaDiFile la parola di listaParole che appare piu` volte
nel file. Cio` deve essere fatto con un processo separato per ogni file di listaDiFile e le
stampe devono essere effettuate nell’ordine in cui terminano i processi. Il callable usato
per effettuare la ricerca nel singolo file deve prendere in input la lista di parole e il nome
del file."""
import multiprocessing
import re


def cerca(listaParole, listaDiFile, occorrenza):
    jobs = multiprocessing.JoinableQueue()

    creaProcessi(jobs, occorrenza)

    addJobs(jobs, listaParole, listaDiFile)

    jobs.join()

def creaProcessi(jobs, occorrenza):
    for _ in range(occorrenza):
        process = multiprocessing.Process(target=worker, args=(jobs,))
        process.daemon = True
        process.start()

def addJobs(jobs, listaParole, listaDiFile):
    for i in range(len(listaDiFile)):
        jobs.put((listaParole,listaDiFile[i]))

def worker(jobs):
    while True:
        try:
            parole,nomeFile = jobs.get()
            occorrenza = cercaParole(parole,nomeFile)
            print("La parola che compare di più nel file {} è: {} ".format(nomeFile,occorrenza))
        except:
            pass
        finally:
            jobs.task_done()

def cercaParole(parole,file):
    f= open(file,"r")
    diz = {}
    testo = f.readlines()
    for i in range(len(parole)):
        occorrenza = re.findall(parole[i],str(testo))
        diz[parole[i]] = len(occorrenza)
    max_key = max(diz, key=diz.get)
    return max_key


def main():
    files = ["file1", "file2", "file3", "file4"]
    parole = ["computer", "very", "with", "algorithms"]

    cerca(parole, files, 4)


if __name__ == "__main__":
    main()

"""  Ecco cosa deve essere stampato (l'ordine delle righe potrebbe cambiare):

La stringa della lista ['computer', 'very', 'with', 'it', 'algorithms'] che appare piu` della altre nel file file1 e` "computer".
La stringa della lista ['computer', 'very', 'with', 'it', 'algorithms'] che appare piu` della altre nel file file2 e` "very".
La stringa della lista ['computer', 'very', 'with', 'it', 'algorithms'] che appare piu` della altre nel file file4 e` "with".
La stringa della lista ['computer', 'very', 'with', 'it', 'algorithms'] che appare piu` della altre nel file file3 e` "algorithms".
"""