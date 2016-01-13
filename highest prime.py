import math
def isprime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

def highest_prime_factor(n):
    for i in range(n-1, 0, -1):
        if n % i == 0 and isprime(i):
            return i

z = highest_prime_factor(13)
print(z)
            
            
    
