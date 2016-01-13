def cs50_inserstion_sort(l):
    for i in range(1, len(l)):
        j = i 
        while j>0 and l[j-1] > l[j]:
            l[j-1], l[j] = l[j], l[j-1]
            j -= 1

mylist = [6, 5, 2, 6, 32, -1, -5, -9, -4]
cs50_inserstion_sort(mylist)
print(mylist)

