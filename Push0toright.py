def Push0toRight(arr):
    for i in range(0, len(arr)):
        for j in range(i, 0, -1):
            if l[j] == 0:
                l[j], l[j-1] = l[j-1], l[j]

l = [0, 3, 4, 5, 0, -2, 12, 0, 2, -5]
Push0toRight(l)
print(l)
