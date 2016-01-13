def is_sorted(l):
    if len(l) == 0 or len(l) == 1:
        return("nothing to sort")
    i = 0
    while i<(len(l)-1):
        if l[i] <= l[i+1]:
            i += 1
            continue
        else:
            return False
    return True

z = is_sorted([])
print(z)
        
