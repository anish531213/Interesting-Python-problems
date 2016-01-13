def hcf(a, b):
    n = 1
    z = 1
    while n != 0:
        if (a/n) == (a//n):
            x = a/n
        while n!= 0:
            if (b/n) == (b//n):
                y = b/n
            if x == y:
                z *= y
            n += 1
        n += 1
        return z

hc = hcf(3, 9)
