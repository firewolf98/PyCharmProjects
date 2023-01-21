


'''togliere i triplici apici se si e` certi di aver fatto bene l'esercizio 2

@DecoratorFactClass(DecoratorFactF(4))
class MyClass1:
   
    def somma(a,b,c):
        return a+b+c




try:
    print(MyClass1.somma("a",3,4,6))
except TypeError as e:
    print(e)
try:
    print(MyClass1.somma("a",3,4))
except TypeError as e:
    print(e)
      
'''

print()
@DecoratorFactClass(staticmethod)
class MyClass2:
    def somma(a,b,c):
        return a+b+c
    
@DecoratorFactClass(staticmethod)
class MyClass3:

    class Inner:
        def __init__(self,a):
            self.b=a
    
            
    def somma(a,b,c):
        return a+b+c
    def metodo(self):
        print("ciao")

    triplica=lambda x:  3*x


print()
istanza2=MyClass2()
istanzaInn=MyClass3.Inner(6)
istanza3=MyClass3()

try:
    x=istanza2.somma(1,2,3)
except TypeError :
    print("Il decoratore di classe non funziona perche' non ha applicato il decoratore a somma")
else:
    print("Tutto ok: la somma e` ",x)

try:
    x=istanza3.somma(7,2,3)
except TypeError :
    print("Il decoratore di classe non funziona perche' non ha applicato il decoratore a somma")
else:
    print("Tutto ok: la somma e` ",x)

try:
    istanza3.metodo()
except TypeError :
    print("Tutto ok: il decoratore e` stato applicato a metodo che e` diventato statico e ha quindi bisogno di ricevere un argomento") 
else:
    print("Il decoratore di classe non funziona perche' non ha applicato il decoratore a metodo")


try:
    x=istanza3.triplica(7)
except TypeError :
    print("Il decoratore di classe non funziona perche' non ha applicato il decoratore a triplica")
else:
    print("Tutto ok: 7*3 = ",x)
    
"""
Il programma deve stampare: (ignorate le prime due linee se non avete tolto la coppia di triplici apici nel codice in alto)

13
somma() missing 1 required positional argument: 'c'


Tutto ok: la somma e`  6
Tutto ok: la somma e`  12
Tutto ok: il decoratore e` stato applicato a metodo che e` diventato statico e ha quindi bisogno di ricevere un argomento
Tutto ok: 7*3 =  21
"""
