def FirstEvenElement(lst):
    d = {}
    for i in lst:
        d[i] = d.get(i, 0) + 1
    for j in lst:
        if d[j] % 2 == 0:
            return j

print(FirstEvenElement([1, 3, 1, 3, 2, 1]))
