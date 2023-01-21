def funz(a,b,*c):
    print(a)
    print(b)
    print(c)
    print(len(c)+2)
    print(len(c))
    d=a+b
    for x in c:
        d=d+x
    print(d)

funz(1,3,4,2,5,6)