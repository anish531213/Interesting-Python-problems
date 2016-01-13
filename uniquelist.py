def unique_list(l):
    if len(l) == 0:
        return ('No elements in list')
    for i in range(0, len(l)):
        for j in range((i+1), len(l)):
            if l[i] == l[j]:
                return False
            else:
                continue
    return True

z = unique_list(['a'])
print(z)
    
