def IsPermutation(string1, string2):
    d = {}
    for i in string1:
        z = d.get(i, 0)
        z += 1
        d[i] = z
    for j in string2:
        if j in d:
            d[j] -= 1
    for keys in d:
        if d[keys] != 0:
            return False
    return True

print(IsPermutation('anish', 'sihna'))
