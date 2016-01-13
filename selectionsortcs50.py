def cs50_selection_sort(l):
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[j] < l[i]:
                l[i], l[j] = l[j], l[i]

mylist = [59, 74, 123, 2, 3, -5, 2, 8]
cs50_selection_sort(mylist)
print(mylist)
