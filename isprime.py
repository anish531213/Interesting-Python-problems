def IsPrime(n):
    m = 1
    i = 0
    while m<=n:
        if n%m == 0:
            i += 1
        m += 1
    if i == 2:
        return True
    else:
        return False
        
answer = IsPrime(13)
print('IsPrime: expected True, got', answer)
