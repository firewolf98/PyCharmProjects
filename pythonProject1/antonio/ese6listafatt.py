import itertools

def fatt(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fatt(n-1)

def f(l):
    listreturn = []
    print(fatt(len(l)))
    listreturn = list(itertools.permutations(l))
    return listreturn



l = [1, 2, 3, 4]
print(f(l))
