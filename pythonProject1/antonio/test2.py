#creare una funzione (documentandola e utilizzando le annotazioni) che crea una lista di n elementi passati in base alle keyword quadrato (t si fa il quadrato f no)
#utilizzare un dizionario per decidere se effettuare una somma o una moltiplicazione della lista dei soli elementi pari o dei soli elementi dispari
#prendendo i comandi in input


def quadrato(lista=[], *args, quad="f", **kwargs) -> list:
    ''' creo una lista
        e la aggiorno ogni volta in
        alla keyword fornita
    '''
    tot = 0
    if quad == "f":
        for x in args:
            lista.append(x)
    else:
        for x in args:
            lista.append(x*x)
    if kwargs.get("op") == "s":
        if kwargs.get("tipo") == "p":
            for val in lista[0::2]:
                tot = tot + val
        if kwargs.get("tipo") == "d":
            for val in lista[1::2]:
                tot = tot + val
    if kwargs.get("op") == "m":
        tot = 1
        if kwargs.get("tipo") == "p":
            for val in lista[0::2]:
                tot = tot * val
        if kwargs.get("tipo") == "d":
            for val in lista[1::2]:
                tot = tot * val
    print("Il totale è {}".format(tot))

    return lista



l = []
print(quadrato.__doc__)
print(quadrato.__annotations__)
#print(quadrato(l, 1, 2, 3, quad="twddsa"))
#print(quadrato(l, 1, 2, 3))
dict = {}
x = input("Inserisci somma o moltiplicazione (s/m)")
dict.update({"op": x})
y = input("Inserisci pari o dispari(p/d)")
dict.update({"tipo": y})
print(quadrato(l, 1, 2, 3, 4, quad="f", **dict))
