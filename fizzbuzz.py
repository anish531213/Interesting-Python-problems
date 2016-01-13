def fizzbuzz(m, n):
    while n>=m:
        z = ''
        if m%3 == 0:
            z += 'Fizz'
        if m%5 == 0:
            z += 'Buzz'
        if m%3 != 0 and m%5 != 0:
            print(m)
        else:
            print(z)
        m += 1
            
fizzbuzz(1, 100)
            
    
