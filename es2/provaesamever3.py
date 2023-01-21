import functools

def coroutine(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        generator = function(*args, **kwargs)
        next(generator)
        return generator
    return wrapper

def funzionericerca(testo, stringa):
    for line in testo.split():
        if(line == stringa):
            return True
    return False


@coroutine
def stamparisultato(stringhe, files):
    while True:
        risultato = (yield)
        if risultato == True:
            print("ok")
        else:
            print("nook")

@coroutine
def gestore(r,stringa):
    while True:
        testo = (yield)
        print(r)
        result = funzionericerca(testo, stringa)
        r.send(result)

def gestisci(listafile, listaparole):
    s = stamparisultato(listaparole, listafile)
    gestori = dict()
    for x2 in listaparole:
        print(type(s))
        gestori[x2] = gestore(s,x2)
    try:
        for i, (file, stringa) in enumerate(zip(listafile, listaparole)):
            print(i)
            testo = open(file, "r").read()
            gestori[stringa].send(testo)
    finally:
        for x in gestori.values():
            x.close()
        s.close()



if __name__ == '__main__':
    files = ["wewe.txt", "wewe2.txt", "wewe3.txt"]
    stringhe = ["panca", "Trento", "entrarono"]
    gestisci(files, stringhe)