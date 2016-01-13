def PrintNonRepeated(string):
    d = {}
    for i in string:
        tmp = d.get(i, 0)
        tmp += 1
        d[i] = tmp
    for i in string:
        if d[i] == 1:
            return i

print(PrintNonRepeated('mornrmnigmoing'))
