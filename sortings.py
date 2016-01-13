

# lets do with mergesort

def SortString2(lst):
    if len(lst)> 1:
        m = len(lst)//2
        left = lst[:m]
        right = lst[m:]

        SortString2(left)
        SortString2(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1

lste = [0, 5, 9, 1, 3, -13]
SortString2(lste)
print(lste)

