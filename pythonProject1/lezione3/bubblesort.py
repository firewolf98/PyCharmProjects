def bubble_sort(a):
    n = len(a)
    while n > 0:
        for i in range(0, n - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
        n -= 1
    return a


a=[5,3,2,4,1]
print(a)
b=bubble_sort(a[:])
print(a)
print(b)
