"""Scrivere la classe FSet che estende frozenset in modo tale che quando si crea un’istanza di
FSet , l’istanza di FSet creata contenga solo gli elementi di ordine dispari dell’oggetto
iterabile (il primo, il terzo, ecc.) passata come argomento a FSet(). Se FSet() non prende
input niente allora l’istanza creata è vuota.
NB: gli elementi di ordine dispari corrispondono agli elementi di indice pari."""


class FSet(frozenset):
    def __new__(cls, *args):
        if args != None:
            a = list()
            for i, e in enumerate(*args):
                if i % 2 == 0:
                    a.append(e)

            obj = super().__new__(cls, a)
            return obj


if __name__ == "__main__":

    fs = FSet([1,2,3,4,5,6,7,8,9,10])
    print(fs)

    frozeli = frozenset()
    print(frozeli)
    ins = set()
    print(ins)
    print(vars(fs))
    print(fs.__dir__())