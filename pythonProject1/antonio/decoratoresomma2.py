def powerUp(f):
    def funz(*args, **kwargs):
        l = []
        for n in args:
            if isinstance(n, list):
                l.extend(n)
            else:
                l.append(int(n))
        return f(*l)
    return funz



@powerUp
def function(*args):
    return sum(args)


if __name__ == "__main__":

    print(function(1, [2, 10], '3'))
