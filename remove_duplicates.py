def remove_duplicates(l):
    new = []
    for i in l:
        if i not in new:
            new.append(i)
    return new

z = remove_duplicates([1, 2, 3, 3, 3, 5])
print(z)
            
        
