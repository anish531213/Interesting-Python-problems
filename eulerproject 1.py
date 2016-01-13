def euler_p1(n):
    count = 0
    for i in range(0, n):
        if i%5 == 0 or i%3 == 0:
            count += i
    return count

z = euler_p1(100)
print(z)
    
