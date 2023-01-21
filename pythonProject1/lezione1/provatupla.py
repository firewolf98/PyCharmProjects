def funz():
    t=(1,3,4)
    print(t)
    t1=3,5,6
    print(t1)
    x,y,z=t
    print(y)
    print(type(z))
    x1,y1,z1=t1
    print(x1)
    print(y1)
    print(z1)
    lst=[1,2,3]
    t2=(lst,4)
    print(lst)
    print(t2)
    lst.append(5)
    print(lst)
    print(t2)
    lst[0]=0
    print(lst)
    print(t2)

funz()