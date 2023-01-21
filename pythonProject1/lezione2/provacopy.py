
def funz():
    lst=[1,3,["ab","bc"]]
    print(lst)
    lst1=lst.copy()
    print(lst1)
    lst1[0]="c"
    print(lst1)
    print(lst)
    lst1[2][1]="cb"
    print(lst1)
    print(lst)




funz()