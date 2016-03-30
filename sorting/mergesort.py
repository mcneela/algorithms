def merge(A, B):
    merged = []
    while A and B:
        if A[0] > B[0]:
            merged.append(B[0])
            B.pop(0)
        else:
            merged.append(A[0])
            A.pop(0)
    while A:
        merged.append(A[0])
        A.pop(0)
    while B:
        merged.append(B[0])
        B.pop(0)
    return merged

def mergesort(A):
    n = len(A)
    if n == 1:
        return A
    left = A[:(n//2)]
    right = A[(n//2):]
    
    left = mergesort(left)
    right = mergesort(right)
    return merge(left, right)
