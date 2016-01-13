import random

def Suffle(l):
    i = 0
    while i < len(l)-1:
        j = random.randint(i, len(l)-1)
        l[i], l[j] = l[j], l[i]
        i += 1

lst = [1, 3, 7, 9, 4, 6]
Suffle(lst)
print(lst)
            
