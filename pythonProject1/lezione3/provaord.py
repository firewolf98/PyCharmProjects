from lezione3.bubblesort import bubble_sort
from lezione3.insertionsort import insertion_sort


def ordina(a, metodo, copia=True):
    if copia:
        return metodo(a[:])
    else:
        return metodo(a)


l1 = [1, 3, 6, 2, 8, 4]
l2 = [1, 3, 6, 2, 8, 4]
b = ordina(l1, bubble_sort)
print('l1=', l1)
print('b=', b)
c = ordina(l2, insertion_sort, False)
print('l2=', l2)
print('c=', c)
