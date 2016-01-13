def sum_0(l):
    new = []
    dn = dict()
    dp = dict()
    for i in l:
        if i >= 0:
            z = dp.get(i, 0)
            z += 1
            dp[i] = z
        else:
            z = dn.get(i, 0)
            z += 1
            dn[i] = z

    for j in dp:
        if (-j) in dn:
            new.append((j, -j))

    return new

z = sum_0([1, -1, 3, 2])
print(z)
