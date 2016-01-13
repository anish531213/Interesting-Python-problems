def BubbleSort(lst):
    for i in range(len(lst), 0, -1):
        for j in range(i):
            if lst[j] < lst[j-1]:
                lst[j], lst[j-1] = lst[j-1], lst[j]

lst = [5, 8, 1, 0, 2, -5, 0]
BubbleSort(lst)
print(lst)
