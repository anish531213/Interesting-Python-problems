from math import *
def highest_prime_factor(n):
    z = sqrt(n)
    i = 2
    while i < n  and n != 1:
        if n % i == 0:
            n = n/i
        else:
            i += 1
    return i

z = highest_prime_factor(26)
print(z)
