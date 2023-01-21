def insertion_sort(a):
    for i in range(1,len(a)):
        val=a[i]
        j=i-1
        while(j>=0 and a[j]>val):
            a[j+1]=a[j]
            j=j-1
            a[j+1]=val
    return a


def ordina(lista,metodo,copia=True):
    if copia==True:
        return metodo(lista[:])
    else:
        return(metodo(lista))


a=[4,5,2,7,1,6]
print(a)
b=ordina(a,insertion_sort)
print(a)
print(b)
b=ordina(a,insertion_sort,False)
print(a)
print(b)
