def sum_N(A, N):
    d = dict()
    l = []
    for i in A:
        if (N-i) not in d:
            d[i] = 1
        else:
            l.append((i, N-i))

    return l

z  = sum_N([1, 2, 3, 5, 5, 9], 10)
print(z)
        
    
