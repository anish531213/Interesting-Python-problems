def is_sorted(l):
    i = 0
    if len(l) == 0:
        return('no elements in list')
    elif len(l) == 1:
        return True
    else:
        while i <= len(l) -2:
            if l[i] <= l[i+1]:
                i += 1
                continue
            else:
                return False
        return True 

z = is_sorted([3, 5, 7, 9, 11, 19, 99, 1])
print(z)
    
