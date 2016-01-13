'''def IsPerfect(n):
    i = 1
    m = 0
    while i < n:
        if n%i == 0 :
            m += i
        i += 1
    if m == n:
        return True
    else:
        return False

answer = IsPerfect(496)
print('IsPerfect: expected True, got', answer)
'''
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

answer = IsPrime(11)
print('IsPrime: expected True, got', answer)


