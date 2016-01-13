def return_unique(s):
    new = []
    for i in s:
        if i in new:
            continue
        else:
            new.append(i)
    return new

z = return_unique([1, 2, 5, 6, 5])
print(z)
            
        
            
