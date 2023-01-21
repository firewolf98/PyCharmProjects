def powerUp(f):
    def funz(*args, **kwargs):
        l = [int(n) for n in args]
        return f(*l)
    return funz



@powerUp
def function(*args):
    return sum(args)


print(function(1, '2', 3))
