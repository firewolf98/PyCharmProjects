import itertools
import collections
import copy

Exam = collections.namedtuple("Exam", "name cfu")
Tripla = collections.namedtuple("Tripla", "esami inglese data")
class observer:
    def __init__(self):
        self.__osservatore = set()

    def add_osservatore(self, influenzato, *influenzati):
        for influenzat in itertools.chain((influenzato,), influenzati):
            self.__osservatore.add(influenzat)
            #influenzat.aggiorna(self)

    def del_osservatore(self, influenzato):
        self.__osservatore.discard(influenzato)

    def notifica_influenzati(self):
        for influenzato in self.__osservatore:
            influenzato.aggiorna(self)


class Laurea_T(observer):

    def __init__(self):
        super().__init__()
        self.__total_cfu = 0
        self.__english_r = False
        self.grades = dict()

    @property
    def total_cfu(self):
        return self.__total_cfu

    @total_cfu.setter
    def total_cfu(self, amount):
        self.__total_cfu += amount

    @property
    def english_r (self):
        return self.__english_r

    @english_r.setter
    def english_r(self, value):
        self.__english_r = value
        self.notifica_influenzati()

    def add_grades(self, exam, voto):
        if exam.name not in self.grades:
            self.grades[exam.name] = voto
            self.total_cfu = exam.cfu
            self.notifica_influenzati()

class ListView:
    def __init__(self):
        self.esami = dict()
        self.inglese = False

    def aggiorna(self, oggetto):
        if oggetto.english_r != self.inglese:
            print("Inglese cambiato")
            self.inglese = True
        elif self.esami == oggetto.grades:
            print("Cambio stato: lo studente ha superato un nuovo esame")
            print("Cambio stato: il numero di CFU e` : ", oggetto.total_cfu, "\n")
            self.esami = copy.deepcopy(oggetto.grades)

class HystoryView:
    def __init__(self):
        self.esami = []

    def aggiorna(self, oggetto):
        #tupla = (1, oggetto.english_r, "10/10/10")
        self.esami.append((copy.deepcopy(oggetto.grades), oggetto.english_r, "10/10/10"))
        for x in self.esami:
            print(x)


if __name__ == '__main__':
    stud = Laurea_T()
    lw = ListView()
    hw = HystoryView()
    stud.add_osservatore(lw, hw)
    stud.english_r = True
    stud.add_grades(Exam("MMI",6), 30)
    stud.add_grades(Exam("MMI", 6), 30)
    stud.add_grades(Exam("MMI2", 8), 30)

