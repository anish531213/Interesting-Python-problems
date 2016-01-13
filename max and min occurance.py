def occourance(l, n):
    for i in range(0, len(l)):
        if l[i] == n:
            last= i
    for i in range(0, len(l)):
        if l[i] == n:
            first= i
            break
    return ("the first occurance is at %ith 'index' and the last occurance is at %ith 'index'" %(first, last))

list1 = [5, 2, 3, 4, 5, 5, 7, 8, 5, 9]
z = occourance(list1, 5)
print(z)
     
