def decorator(function):
    def wrapper(*args, **kwargs):
        l = []

        def f(*args):
            for x in args[0]:
                if isinstance(x, list) or isinstance(x, dict):
                    f(x)
                else:
                    try:
                        l.append(int(x))
                    except: pass
        f(*args)
        return function(*l, **kwargs)

    return wrapper


@decorator
def f(*args):
    return sum(args)


print(f(['1', ['2', [4, {"anna":"1"}]], 3]))
