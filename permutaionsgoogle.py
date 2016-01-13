def permutation(s):
    new = []
    for i in s:
        for j in s:
            new.append((i, j))
    return new

z = permutation({1, 3, 4})
print(z)
