def hcf(m, n):
    if m%n == 0:
        return n
    else:
        if m > n:
            hcf(n, m%n)
        else:
            hcf(m, m%n)

z = hcf(2, 3)
print(z)
