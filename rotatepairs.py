def word(l):
    d = dict()
    new = []
    for i in l:
        d[i[::-1]] = 1
    for i in l:
        if i in d:
            new.append(i)
    return  new

z = word(['an', 'ab','na', 'ba', 'ak', 'bk'])
print(z)   
    
