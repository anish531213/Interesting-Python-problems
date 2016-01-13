def hcf(m, n):
    for i in range(m, 0, -1):
        if m % i == 0 and n % i == 0:
            return i

z = hcf(12, 18)
print(z)
