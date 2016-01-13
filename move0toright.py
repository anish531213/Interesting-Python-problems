def move_0(l):
    for i in range(len(l)-1):
        for j in range(0, len(l)-1-i):
            if l[j] == 0:
                l[j+1] , l[j] = l[j], l[j+1]

mylist = [1, 2, 4, 0, 0, 12]
move_0(mylist)
print(mylist)

def move0(l):
    new = []
    for i in l:
        if i != 0:
            new.append(i)
    for i in l:
        if i == 0:
            new.append(i)
    return new

z = move0([1, 2, 4, 0, 0, 12])
print(z)
            
            
        
