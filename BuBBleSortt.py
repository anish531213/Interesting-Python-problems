def BubbleSort(arr):
    for i in range(len(arr), 0, -1):
        for j in range(i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
l = [3, 9, 7, 1, 3, 4, 8, 2, -1, -5]
BubbleSort(l)
print(l)
