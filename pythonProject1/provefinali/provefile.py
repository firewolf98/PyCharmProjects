def conta(parola, *args):
    for arg in args:
        conta = 0
        file = open("" + arg,'r')
        for r in file:
            parola2 = parola + '\n'
            if r == parola:
                conta = conta + 1
            if r == parola2:
                conta = conta + 1
        print(arg, ':', conta)


conta('ciao', 'file1', 'file2')
