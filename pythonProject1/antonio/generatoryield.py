def generatore(n):
    i = 0
    j = 1
    while j < n:
        yield i
        i += j
        j += 1


for x in generatore(10):
    print(x)

