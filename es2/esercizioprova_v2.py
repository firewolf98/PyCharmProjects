def coroutine(f):
    def wrapper(*args, **kwargs):
        generator = f(*args, **kwargs)
        next(generator)
        return generator
    return wrapper


@coroutine
def onehandle(successor = None):
    while True:
        request = yield
        if 1< request< 11:
            print("Handler Uno")
        else:
           successor.send(request)


@coroutine
def defhandle():
    while True:
        request = yield
        print("Default")


if __name__ == '__main__':
    c = onehandle()
    c.send(2)
    c.send(12)



