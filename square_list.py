def square_list(l):
    new = []
    i = 0
    j = len(l) - 1
    while i <= j:
        if l[i]**2 <= l[j]**2:
            new.append(l[i]**2)
            i += 1
        elif l[j]**2 > l[i]**2:
            new.append(l[j]**2)
            j -= 1
    return new

z = square_list([-5, 1, 3, 5])
print(z)
        
    
        
