def EvenFibonacciNumbers(n):
    if n == 1:
        return 0
    a = 0
    b = 1
    i = 2
    sumn = 0
    while i < n:
        b = a+b
        a = b-a
        if b %2 == 0:
            sumn += b
        i += 1
    return sumn

print(EvenFibonacciNumbers(7))

        
        
