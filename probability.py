import random



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

def createlist():
    t = []
    k = 0
    while k < 23:
        t.append(random.randint(1, 365))
        k += 1
    return t



def find_probable():
    count = 0
    for index in range(1, 1001):
        t = createlist()
        if unique_list(t):
            count += 1
    return count

z = find_probable()
print(z)
