def pair(A, N):
    d = dict()
    l = []
    for i in A:
        z = d.get(i, 1)
        z += 1
        d[i] = z
    for j in A:
        if (N-j) == j:
            del d[j]
        if (N-j) in d:
            l.append((j, N-j))
            del d[j]
    return l

z = pair([2, 3, 5, 8], 10)
print(z)
                                                                                      
    
