def f(k):
    for j in range(0, k):
        print("Numero stampato {}".format(j))


f(5)
f(10)
x = [(i, j, k) for i in range(0,11) for j in range (0, 11) for k in range (0,11)]
print(x)

#Definire una lista con 50 elementi; dei dispari si effettua la stampa, dei pari si crea un dizionario con i quadrati e alla fine si stampa

l = [i for i in range(0, 50)]
print(l)
i = 0
for x in l[1::2]:
    print(x)

dic = {}
for y in l[0::2]:
    print(y)
    dic.update({str(y): y*y})
print(dic)



