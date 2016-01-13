def hcf(m, n):
    if m>n:
        if m%n == 0:
            return (n)
        else:
            hcf(n, m%n)

    else:
        if n%m == 0:
            return (m)
        else:
            hcf(m, n%m)

z = hcf(8, 12)
print(z)
