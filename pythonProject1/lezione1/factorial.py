def factorial(n):
    result=1
    for k in range(1,n+1):
        result=result*k
    return result



print("fattoriale di 3",factorial(3))
print("fattoriale di 5",factorial(5))