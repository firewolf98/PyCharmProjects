def applica(da_fare):
    resultList = []
    tipo,*args=da_fare[0]
    istanza=tipo(*args)
    for t in da_fare[1:]:
        meth,*args=t
        result=meth(istanza,*args)
        resultList.append(result)
    return resultList


class Classe:
    val = 8

    def f(self, x, y):
        return x + y

    def g(self, *args):
        return args[0] * args[1] + Classe.val


class AltraClasse:
    def __init__(self, v):
        self.val = v

    def f(self, x, y):
        return x + y

    def g(self, *args):
        return args[0] * args[1] + self.val


def main():
    coseDaFare1 = ((Classe,), (Classe.f, 3, 4), (Classe.g, 2, 5))
    coseDaFare2 = ((AltraClasse, 6), (AltraClasse.f, 5, 6), (AltraClasse.g, 2, 5))
    l1 = applica(coseDaFare1)
    l2 = applica(coseDaFare2)
    print("la prima lista dei risultati e`:", l1)
    print("la seconda lista dei risultati e`:", l2)


if __name__ == '__main__':
    main()

"""Il programma deve stampare:
la prima lista dei risultati e`: [7, 18]
la seconda lista dei risultati e`: [11, 16]
"""
