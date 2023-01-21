def fact(n):
    result = 1
    for k in range(1, n + 1):
        result = result * k
    return result


def provaliste():
    l = list('ciao')
    print(l)
    l.append('x')
    print(l)
    l.insert(3, 3)
    print(l)
    l1 = list('miao')
    l.extend(l1)
    print(l1)
    print(l)
    print(len(l))
    l2 = list('pio')
    l1 += l2
    print(l1)
    l1.pop()
    print(l1)
    l1.pop(3)
    print(l1)
    print(l2)
    l2.clear()
    print(l2)
    l1.sort()
    print(l1)


def provatuple():
    t = (1, 'c', 3)
    x, y, z = t
    print(t)
    print(x)
    print(y)
    print(z)
    l = list('ciao')
    g = (l, 'miao')
    print(l)
    print(g)
    l.extend('2')
    print(l)
    print(g)
    l.clear()
    print(l)
    print(g)


def provaset():
    s = set('miao')
    print(s)
    s.add('ciao')
    print(s)
    s.add('o')
    print(s)


def provadict():
    d = {'luca': '338', 'mirco': '334'}
    print(d)
    d['ely'] = '232'
    print(d)
    chiavi = d.keys()
    print('chaivi=', chiavi)
    valori = d.values()
    print('valori=', valori)
    for i in chiavi:
        print(i)
    for i in d.values():
        print(i)
    elem = d.items()
    for i, j in elem:
        print(i, j)
    for k in elem:
        print(k)


def provaoper():
    """
    serve per provare le operazioni

    """
    l=list('c')
    print(l)
    l = l * 3
    print(l)
    a = 3
    b = 4
    c = 5
    if a < b < c:
        print('ciao')
    if 3 < b + c < 10:
        print('ciao')
    massimo = a if a > b else b
    print(massimo)
    l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(l1)
    l2 = [x for x in l1 if x>3]
    print(l2)
    l3 = [(x, y) for x in l1 for y in l1 if x > 2 and y > 5]
    print(l3)


#print("fact di 3", fact(3))
#provaliste()
#provatuple()
#provaset()
#provadict()
#provaoper()
print(provaoper().__doc__)
