def histogram(s):
    d = dict()
    for c in s:
        z = d.get(c, 0)
        z += 1
        d[c] = z


    return d

z = histogram('anisha')
print(z)
