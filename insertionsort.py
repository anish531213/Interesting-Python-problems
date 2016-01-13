def insertion_sort(l):
    for i in range(1, len(l)):
        j = i-1
        while l[j+1] < l[j] and j >= 0:
            l[j], l[j+1] = l[j+1], l[j]
            j -= 1

mylist = [1, 2, 3, 5, 2, 2, 1, 3, -1]
insertion_sort(mylist)
print(mylist)
