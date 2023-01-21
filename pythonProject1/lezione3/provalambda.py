def f(x):
    return x*x

g=lambda x:x*x

print(f(3))
print(g(3))

dati=[1,-2,5,-4,6]
print(dati)
dati.sort(key=lambda x:abs(x))
print(dati)

