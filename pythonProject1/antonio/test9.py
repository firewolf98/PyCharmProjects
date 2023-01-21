def fibonacci(n):
    if n == 0:
        return 0
    elif n == 2 or n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacciYield(n, prec, parz):
    print("n = ", n)
    if n == 0:
        yield 0
    elif n == 1:
        yield 1
    elif n == 2:
        print("parz ", parz, "prec ", prec)
        yield fibonacciYield(1, 0, 0)
        yield 1


    else:

        prec, parz = parz, (parz + prec)
        yield parz
        yield from fibonacciYield(n - 1, prec, parz)


for x in fibonacciYield(4, 1, 1):
    print(x)