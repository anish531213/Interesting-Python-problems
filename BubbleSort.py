def BubbleSort(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-i-1):
            if lst[j+1] < lst[j]:
                lst[j+1], lst[j] = lst[j], lst[j+1]

lst = [80, 79, 3, 4, 0, -13, -9]
BubbleSort(lst)
print(lst)
