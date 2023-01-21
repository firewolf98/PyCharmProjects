def convertitore(f):
    def wrapper(*args, **kwargs):
        lista = [int(arg) for arg in args[0]]
        print(lista)
        return f(*lista, **kwargs)
    return wrapper


@convertitore
def f(*args):
    return sum(args)


print(f([1, 2, '34']))
