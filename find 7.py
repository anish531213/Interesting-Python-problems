def find_7(n):
    if n == 0:
        return 0
    elif (n%10) == 7:
        return(1 + find_7(n//10))
    elif (n%10) != 7:
        return(0 + find_7(n // 10))
    
z = find_7(777)               
print(z)
    
