def sum_N(A, N):
    new = []
    for i in A:
        A.remove(i)
        if (N-i) in A:
            new.append((i, N-i))
    return new

z = sum_N([1, 2, 3, 4,4, 4, 5], 8)
print(z)      
