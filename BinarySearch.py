def BinarySearch(lst, key, midpoint):
    if key == lst[0]:
        return 0
    if key == lst[midpoint]:
        return midpoint
    else:
        if key < lst[midpoint]:
            return BinarySearch(lst, key, midpoint - len(lst[:midpoint])//2)
        else:
            return BinarySearch(lst, key, midpoint + len(lst[midpoint:])//2)

lst = [1, 4, 6, 9]
print(BinarySearch(lst, 1, len(lst)//2))
    
