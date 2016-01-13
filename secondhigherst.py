def SecondHighest(l):
    d = {}
    for i in l:
        d[i] = d.get(i, 0)
    m = max(l)
    del d[m]
    return max(d.keys())

print(SecondHighest([1, 3, 5, 9, 11, 11]))
