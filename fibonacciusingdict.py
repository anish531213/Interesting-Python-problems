# 0 1 1 2 3 5 8 13 21
d = {1: 0, 2: 1}

def fib(n):
    if n in d:
        return d[n]
    else:
        z = fib(n-1) + fib(n-2)
    d[n] = z
    return z

z = fib(6)
print(z)
    
