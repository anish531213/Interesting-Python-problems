def QuickSort(lst, left, right):
    i = left, j = right
    pivot = lst[(left + right)//2]

    while i <= j:
        while lst[i] < pivot:
            i += 1
        while lst[j] > pivot:
            j -= 1
        if  i <= j:
            lst[i], lst[j] = lst[j], tmp[i]
            i += 1
            j -= 1

    if left < j:
        QuickSort(lst, left, j)
    if i < right:
        QuickSort(lst, i, right)

lst = [9, 8, 7, 2, 3, -7, -13]
QuickSort(lst, 0, 6)
print(lst)
