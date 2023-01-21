def scrivisufile():
    st = input("Cosa vuoi scrivere?")
    fp = open('res', 'w')
    fp.write(st)


def leggidafile():
    fp = open('res', 'r')
    st = fp.read()
    print(st)


#scrivisufile()
leggidafile()
