def reversenum(n):
    ans = 0
    while n != 0:
        m = n%10
        ans = ans*10 + m
        n = n//10
    return ans

print(reversenum(456789))
