def new_range(n):
    k=0
    while k<n:
        yield k
        k+=1

for i in new_range(10):
    print(i,end=" ")
