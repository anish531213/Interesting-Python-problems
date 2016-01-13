def bubble_sort(l):
    for i in range(len(l)-1):
        for j in range(0, len(l)-i-1):
            if l[j] > l[j+1]:
                l[j] , l[j+1] = l[j+1], l[j]

mylist = [1, 2, 3, 5, 2, 2, 1, 3, -1]
bubble_sort(mylist)
print(mylist)
