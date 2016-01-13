def merge_sort2(l):
    if len(l) > 1:
        m = (len(l)) // 2
        left = l[:m]
        right = l[m:]

        merge_sort2(left)
        merge_sort2(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                l[k] = left[i]
                i += 1
            else:
                l[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            l[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            l[k] = right[j]
            j += 1
            k += 1

z = [1, 3, -1, 5, 2]
merge_sort2(z)
print(z)
