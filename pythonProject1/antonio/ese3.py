def f(lista, x):
    if len(lista) == 0:
        return False
    y = lista.pop()
    if y == x:
        return True
    else:
        return f(lista, x)


def myDeepCopy(lista):
    if len(lista) == 0: return list([])
    cpyList = []
    for i in lista:
        if not isinstance(i, list):
            cpyList.append(i)
        else:
            tmp = myDeepCopy(i)
            cpyList.append(tmp)
    return cpyList




l = [x for x in range(0, 50)]
print(l)
print(f(l, 10))

li = [1, 2, 3, [4, [5, 6]]]
print(myDeepCopy(li))



