def generator(n):
    i = 0
    j = 1
    while i < n:
        yield i
        i += j
        j += 1


for x in generator(10):
    print(x)





