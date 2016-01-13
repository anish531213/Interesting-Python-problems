def HighestOccurred(string):
    d = {}
    for i in string:
        z = d.get(i, 0)
        z += 1
        d[i] = z
    maxx = d[string[0]]
    temp = None
    for j in d:
        if d[j] > maxx:
            temp = j
            maxx = d[j]
    return temp

print(HighestOccurred('abb'))
