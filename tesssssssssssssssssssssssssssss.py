def IsPerfect(n):
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
