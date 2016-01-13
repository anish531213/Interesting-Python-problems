def min_of_list(l):
    m = l[0]
    for i in l:
        for j in l:
            if j < i:
                m = j
    return m

z = min_of_list([1, 2, 3, 4, 5, -2, -5])
print(z)

#use of dictionaries

def min(n):
    d = {1 : n[0]}
    for i in n:
        if i < d[1]:
            d[1] = i
    return d[1]

k = min_of_list([0, 2])
print(k)
    
    
