def nuoveprove(a, l =[]):
    l.append(a)
    print(l)


def nuoveprove2(a, l =None):
    if(l is None):
        l=[]
    l.append(a)
    print(l)


def argvar(v1, v2=2, *arg):
    print(v1)
    print(v2)
    if(arg):
        print(arg)
    else:
        print('stop')
    for x in arg:
        print(x)


def somma(*addendi3):
    som = 0
    for x in addendi3:
        som = som + x
    print(som)


def provadict(arg1, arg2, **cmd):
    if cmd.get('operazione') == '+':
        print(arg1 + arg2)
    elif cmd.get('operazione') == '-':
        print(arg1 - arg2)
    elif cmd.get('operazione') == '*':
        print(arg1 * arg2)
    else:
        print('operazione non supportata')
    if cmd.get('azione') == 'stampa':
        print('arg1=', arg1, ', arg2=', arg2)
    if cmd.get('saluto') == 'ciao':
        print('Ehy ciao!')
    elif cmd.get('saluto') == 'hi':
        print('puzziat perd!')
    else:
        print('non ti saluto')


#nuoveprove(1)
#nuoveprove(2)
#nuoveprove(3)
#nuoveprove2(1)
#nuoveprove2(2)
#nuoveprove2(3)
#argvar(1)
#argvar(1, 4)
#argvar(1, 4, 3, 5, 6)
#L = [1, 2, 3]
#argvar(1, 6, L)
#argvar(1, 6, *L)
#addendi = [1, 3, 4]
#addendi2 = [3, 6, 2, 1, 4]
#somma(*addendi)
#somma(*addendi2)
provadict(2, 4)
provadict(2, 4, operazione='+')
provadict(2, 4, operazione='-')
provadict(2, 4, operazione='*')
provadict(2, 4, operazione='/')
provadict(2, 4, operazione='+', azione='stampa')
provadict(2, 4, operazione='-', saluto='ciao')
provadict(2, 4, operazione='*', azione='stampa', saluto='hi')
provadict(2, 4, operazione='/', saluto='Hola')
