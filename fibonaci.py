def fibonaci(n):
    temp = 0
    if n == 1 or n == 2:
        return 1
    elif n == 0:
        return 0
    else:
        temp = fibonaci(n-1) + fibonaci(n-2)
        return temp
x = fibonaci(6)
print(x)
        
