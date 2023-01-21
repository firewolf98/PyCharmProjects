def coroutine(f):
    def wrapper(*args, **kwargs):
        generatore = f(*args, **kwargs)
        next(generatore)
        return generatore
    return wrapper

@coroutine
def Handler_04(successor):
    while True:
        list = yield
        if 0 < list[0] < 5:
            print("Richiesta {} gestita da handler_04".format(list))
        else:
            successor.send(list)


@coroutine
def Handler_59(successor):
    while True:
        list = yield
        if 4 < list[0] < 10:
            print("Richiesta {} gestita da handler_59".format(list))
        else:
            successor.send(list)

@coroutine
def Handler_default(successor):
    while True:
        list = yield
        if list[0] < 0:
            print("Richiesta {} gestita da handler_default : non è stato possibile gestire la richiesta".format(list))
        else:
            successor.send(list)

@coroutine
def Handler_gt9():
    while True:
        list = yield
        print("Messaggio da Handler_gt9: non e` stato possibile gestire la richiesta {}. Richiesta modificata".format(list))
        list[0] -= list[1]
        g = Handler_default(Handler_04(Handler_59(Handler_gt9())))
        g.send(list)


if __name__ == '__main__':
    g = Handler_default(Handler_04(Handler_59(Handler_gt9())))
    g.send([11, 2])

