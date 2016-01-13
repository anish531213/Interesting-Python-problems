def recurse_sum(n):
    if n != 0:
        sumn = n + recurse_sum(n-1)
    return(sumn)


z = recurse_sum(5)
print(z)
    
    
