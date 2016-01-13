'''
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
       
        c= (fib(n-1) + fib(n-2))
        print (c)
    return c
f = fib(5)
print(f)
'''


def fib(n):

    a=0
    b=1
    temp=0
    print (a)
    for i in range(n):      
        temp=a
        a=b
        b=temp+b

        temp=0
        print (b)

fib(8)
        

