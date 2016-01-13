import math

def TotalLockPatterns():
    sumn = 0
    for i in range(4, 10):
        sumn += math.factorial(10)/math.factorial(10-i)
    return sumn

print(TotalLockPatterns())
