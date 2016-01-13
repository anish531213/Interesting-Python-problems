def QuickSort(arr):
    less = []
    greater = []
    equal = []

    if len(arr) > 1:
        pivot = arr[len(arr)-1]
        for x in arr:
            if x < pivot:
                less.append(x)
            elif x > pivot:
                greater.append(x)
            else:
                equal.append(x)
        return QuickSort(less)+equal+QuickSort(greater)
    else:
        return arr

print(QuickSort([2, 9, 7, -1, -6, 0, 2, 3, 4, 8]))
