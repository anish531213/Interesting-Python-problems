#first method
'''
def differs(A, k):
    pairs = []
    for i in range(len(A)):
        for j in range(len(A)):
            if i != j:
                if k + A[i]== A[j]:
                    pairs.append((A[i], A[j]))
    return pairs

z = differs([1, 2, 3, 5, 6, 8, 9, 11, 12, 13], 3)
print(z)
'''
#second method

def differs(A, k):
    l = []
    d = {}
    for i in range(len(A)):
        d[A[i]] = i
    for j in range(len(A)):
        temp = k + A[j]
        if temp in d:
            l.append((A[j], temp))
            del d[A[j]]
    return l

z = differs([1, 2, 3, 5, 6, 8, 9, 11, 12, 13], 3)
print(z)
