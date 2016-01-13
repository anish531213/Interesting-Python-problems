def equivalent(l1, l2):
    d = dict()
    for i in l1:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    for j in l2:
        if j in d:
            d[j] -= 1

    for e in d:
        if d[e] != 0:
            return False

    return True

z = equivalent([1, 2, 3, 9], [2, 1, 3])
print(z)
