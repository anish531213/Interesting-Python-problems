def sum_N(A, N):
    new = []
    d = dict()
    z = 0
    for i in A:
        z = d.get(i, z)
        z += 1
        d[i] = z
    for i in A:
        d.pop(i)
        if (N-i) in d:
            new.append((i, N-i))
    return new

z = sum_N([1, 2, 3, 4, 4, 4, 5], 8)
print(z) 
