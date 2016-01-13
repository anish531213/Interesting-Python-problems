def SortString(lst):
    for i in range(len(lst)):
        for j in range(i):
            if len(lst[j+1]) < len(lst[j]):
                lst[j+1], lst[j] = lst[j], lst[j+1]

lst = ['act','keto','akt','a','ante']
SortString(lst)
print(lst)

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
            if len(left[i]) < len(right[j]):
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

lste = ['and','keto','akt','','a','ante']
SortString2(lste)
print(lste)

