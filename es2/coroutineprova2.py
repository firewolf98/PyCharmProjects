def coroutine(function):
    def wrapper(*args, **kwargs):
        generator = function(*args, **kwargs)
        next(generator)
        return generator
    return wrapper

@coroutine
def generatorlist():
    while True:
        x = yield
        yield x+x


@coroutine
def generator():
    l = []
    while True:
        v = yield
        if v == "stop": break
        print(v)
        l.append(v)
        yield v*v

    g = generatorlist()
    for x in l:
        y = g.send(x)
        next(g)
        print("add = ", y)


if __name__ == '__main__':
    print("invio valori a caso")
    g = generator()
    for x in range(11):
        y = g.send(x)
        next(g)
        print("val ", y)
    g.send("stop")

