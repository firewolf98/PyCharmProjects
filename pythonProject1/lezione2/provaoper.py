def funz():
    a=[1,2]
    b=a
    if(a is b):
        print("SI")
    else:
        print("NO")
    if(a==b):
        print("OK")
    else:
        print("!OK")
    c=a.copy()
    if (a is c):
        print("SI")
    else:
        print("NO")
    if (a == c):
        print("OK")
    else:
        print("!OK")
    words=["cat","luca","enrica"]
    for w in words:
        print(w,len(w))

    lst=([k*k for k in range(1,10)])
    print(lst)


funz()