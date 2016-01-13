def rearrange_indices(A, B):
    d = {}
    for i in range(0, len(A)):
        d[A[i]] = B[i]
    for key in d:
        A[d[key]] = key

A = ['c', 'd', 'e', 'f', 'g']
rearrange_indices(A, [3, 0, 4, 1, 2])
print(A)
