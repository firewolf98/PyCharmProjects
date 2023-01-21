def insertion_sort(a):
    for i in range(1, len(a)):
        val = a[i]
        j = i-1
        while j >= 0 and a[j] > val:
            a[j+1] = a[j]
            j = j-1
            a[j+1] = val
    return a


def bubble_sort(a):
    n = len(a)
    while n > 0:
        for i in range(0, n - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
        n -= 1
    return a
