def quicksort(A, p, r):
    if  p < r:
        q = partition(A, p, r)
        quicksort(A, p, q)
        quicksort(A, q + 1, r)

def partition(A, p, r):
    x = A[p]
    i = p - 1
    j = r + 1
    while True:
        while True:
            j = j - 1
            if A[j] <= x:
                break
        while True:
            i = i + 1
            if A[i] >= x:
                break
        if A[j] <= x and A[i] >= x:
            if i < j:
                copy = A[i]
                A[i] = A[j]
                A[j] = copy
            else:
                return j
