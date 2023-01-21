def generator(n):
    if n == 0:
        l = []
        l.append(0)
        return l
    l = generator(n-1)
    x = 0
    while n >= 1:
        x += n
        n -= 1
    l.append(x)
    return l



print(generator(4))
