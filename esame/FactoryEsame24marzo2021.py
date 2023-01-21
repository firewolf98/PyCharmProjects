"""Scrivere nel file esercizio3.py un decorator factory df(L1,L2) che prende in input una lista
di stringhe e una stringa di oggetti e produce un decoratore che fa in modo che le istanze
della classe nascano non solo con le variabili di istanza aggiunte dal metodo __init__ della
classe ma anche con le seguenti variabili di istanza:
• per ogni i =1,…, len(L1), una variabile con nome uguale a quello della i-esima
stringa di L1 e valore uguale all’i-esimo oggetto di L2. Nel caso in cui __init__
della classe originaria aggiungeva gia` una variabile di istanza con nome uguale
all’i-esima stringa di L1 allora il valore della variabile deve essere quello
assegnato da __init__ della classe originaria."""

def df(L1, L2):
    def decorator(aClass):
        old_init = aClass.__init__

        def newInit(self, *args, **kwargs):
            for var, value in zip(L1, L2):
                setattr(self, var, value)
            old_init(self, *args, **kwargs)

        aClass.__init__ = newInit
        return aClass
    return decorator



@df(["v1","v2","v3","v4"],["quando","come",["fuori",21],2])
class C1:
    def __init__(self,z1,z2,z3):
        self.w1=z1
        self.w2=z2
        self.w3=z3

@df(["v1","v2","v3"],["Ecco",{"D":"f"},"spaghetto"])
class C2:
    def __init__(self,*args):
        if len(args)<3:
            print("numero errato di argomenti")
        else:
            self.v3=args[0]
            self.w1=args[1]
            self.w2=args[2]

c=C1('a','b', "dado")
print(c.w1,c.w2,c.w3,c.v1,c.v2,c.v3,c.v4)


c=C2('quadrato','esatto', "cubo",21)
print(c.w1,c.w2,c.v1,c.v2,c.v3)


"""
Il programma deve stampare:

a b dado quando come ['fuori', 21] 2
esatto cubo Ecco {'D': 'f'} quadrato

"""


