d = {'a': 1, 'b': 4, 'o': 2, 'n': 1, 's': 2, 'r': 3, 'u': 2, 't': 1} 

def reverse_lookup(d, v):
    z = []
    for k in d:
        if d[k] == v:
            z.append(k)
    return z
    raise ValueError

z = reverse_lookup(d, 2)
print(z)
