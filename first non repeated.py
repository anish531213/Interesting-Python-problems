def first_non_repeated(lst):
    d = {}
    for i in lst:
        d[i] = d.get(i, 0) + 1
    for i in lst:
        if d[i] == 1:
            return i

print(first_non_repeated([1,1, 3, 4, 2, 3]))
