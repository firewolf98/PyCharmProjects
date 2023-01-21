def ricerca(x, l = []):
    if x == l[0]:
        return True
    else:
        if len(l) == 1:
            return False
        return ricerca(x, l[1::])


print(ricerca(10, [1, 2, 3, 4, 5, 10]))


