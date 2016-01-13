# 0 1 1 2 3 5 8 13
def factorial(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return factorial(n-1) + factorial(n-2)

print(factorial(5))
        
