def bubblesort(A):
    for i in range(0, len(A)):
        for j in range(0, len(A)-1):
            if A[j] > A[j + 1]:
                copy = A[j]
                A[j] = A[j + 1]
                A[j + 1] = copy
