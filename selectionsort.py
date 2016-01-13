def SelectionSort(lst):
    for i in range(len(lst)):
        min = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min]:
                min = j
        if min != i:
            lst[min], lst[i] = lst[i], lst[min]

lst = [80, 79, 3, 4, 0, -13, -9]
SelectionSort(lst)
print(lst)
