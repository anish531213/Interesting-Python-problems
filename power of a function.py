def power(a, b):
    x = a ** (b/2)
    if b % 2 == 0:
        return x*x
    else:
        return x*x*b

print(power(2, 3))
