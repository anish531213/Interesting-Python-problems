def LargestPrime(n):
    i = 2
    while n!= 1:
        if n % i == 0:
            n = n//i
        else:
            i += 1
    return i

print(LargestPrime(9))
