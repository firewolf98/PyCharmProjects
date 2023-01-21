
def raddoppio():
    while True:
        x = yield
        print("Stampa tra uno yield e l'altro del corpo del while. x = ", x)
        x = yield x*2
        print("x = ", x)


g = raddoppio()
r = next(g)
r = g.send(5)
print(r)
r = next(g)

