def every_sum(n):
    while n > 0:
        sumn = 0
        while sumn < n:
            print (n, end = '')
            sumn += 1
        n -= 1
every_sum(3)
