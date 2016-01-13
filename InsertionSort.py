def InsertionSort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if l[j] < l[j-1]:
                l[j], l[j-1] = l[j-1], l[j]

l = [3, 9, 7, 1, 3, 4, 8, 2, -1, -5]
InsertionSort(l)
print(l)
