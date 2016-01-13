def getsum(n):
    total = 0
    for i in range(0, n, 10**i):
        total += i
    return total

print(getsum(550))
