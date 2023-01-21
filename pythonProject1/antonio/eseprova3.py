def myGenerator(n):
    i = 1
    fact = 1
    while i < n + 1:
        fact *= i
        print(fact)

        i += 1


def myGeneratorRec(n,result, i):
    if i == 1:
        yield 1
    else:
        print(i)
        result *= (myGeneratorRec(n, result, i-1))
        yield result





def myGeneratorYield(n):
    yield from myGeneratorRec(n, 1, n)



#for x in myGeneratorYield(2):
#    print(x)

myGenerator(4)
