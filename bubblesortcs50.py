def cs50_bubble_sort(l):
    for i in range(len(l)-1):
        for j in range(0, len(l)-i-1):
            if l[j+1] < l[j]:
                l[j], l[j+1] = l[j+1], l[j]

mylist = [2, 5, 33, 23, 4, -50, -3, -9, 2, 1]
cs50_bubble_sort(mylist)
print(mylist)
