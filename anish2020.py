def identical(l1, l2):
    if len(l1) != len(l2):
        return False
    for i in l1:
        if i in l2:
            l2.pop(l2.index(i))
            continue
        else:
            return False
    return True

z = identical([1, 2, 4, 4], [2, 1, 4, 3])
print(z)    
    
