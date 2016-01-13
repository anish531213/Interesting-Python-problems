def square_list(l, s):
    i = 0
    j = len(l) - 1
    while i < len(l):
        if  (l[i])**2 < (l[j])**2:
            s.append(l[i]**2)
            l.pop(i)
            square_list(l, s)
        else:
            s.append(l[j]**2)
            l.pop(j)
            square_list(l, s)
    return(s)

z = square_list([13, 17, 8 , 2, 1, 3], [])
print(z)    
        
