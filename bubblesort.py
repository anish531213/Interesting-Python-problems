def BubbleSort(l):
    print("in beginning", l)
    for i in range(len(l)-1):
        for j in range(len(l)-1-i):
            if l[j] < l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    print(l)

BubbleSort([1, 5, 5, 9, 2, 4])
