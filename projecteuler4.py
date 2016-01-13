def ReverseNumber(m):
    n = m
    new = 0
    l = []
    while n!= 0:
        l.append(n%10)
        n = n//10
    z = len(l)-1
    for i in l:
        new += i * (10**z)
        z -= 1
    if new == m:
        return True
    return False

        
