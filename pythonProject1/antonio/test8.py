#scrivere un file che contiene la sequenza di fibonacci di x numeri
#creare una lista con i valori all'interno del file
#creare un generatore  della somma degli interi nella lista
#aggiungere le somme parziali alla fine del file

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 2 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def fibseq(n):
    i = 0
    parziale = 1
    parzialeprec = 1
    while i < n:
        if i == 0:
            yield 0
        elif i == 1 or i == 2:
            yield 1
        else:
            parzialeprec, parziale = parziale, (parziale+parzialeprec)
            yield parziale
        i += 1

def sommatore(l):
    tot = 0
    for x in l:
        tot += x
        yield tot


file = open("file", "w")
for x in fibseq(11):
    file.write(str(x) +"\n")
file.close()
file = open("file", "r")
l = [int(x) for x in file.readlines()]
file.close()
file = open("file", "a")
for x in sommatore(l):
    file.write((str(x) + "\n"))
file.close()
