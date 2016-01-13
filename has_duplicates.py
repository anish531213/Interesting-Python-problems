def has_duplicates(l):
    d = dict()
    for i in l:
        if i in d:
            return False
        else:
            d[i] = 1
    return True

z = has_duplicates([1, 2, 3, 'a', 'a'])
print(z)
