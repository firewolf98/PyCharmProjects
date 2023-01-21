def coroutine(function):
    def wrapper(*args, **kwargs):
        generator=function(*args, **kwargs)
        next(generator)
        return generator
    return wrapper


@coroutine
def generator():
    while True:
        v=yield
        print(v)
        yield v*v

if __name__=='__main__':
    print("invio valori a caso")
    g=generator()
    for x in range(4):
        y=g.send(x)
        next(g)
        print('val', y)