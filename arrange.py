import math

def highest_prime(n):
    for i in range(n-1, 0 , -1):
        if n%i == 0 and isprime(i):
            return i

def isprime(num):
    for j in range(2, int(math.sqrt(num))):
        if num%j == 0:
            return False
    return True

z = highest_prime(39)
print(z)

    
        
