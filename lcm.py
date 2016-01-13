def hcf(m, n):
    for i in range(m, 0, -1):
        if m % i == 0 and n % i == 0:
            return i
        
def l(m, n):
    k = m * n
    return (k / hcf(m, n))

z = l(10, l(9, l(8, l(7, l(6, l(5, l(4, l(3, l(2, 1)))))))))
z = int(z)
print(z)
