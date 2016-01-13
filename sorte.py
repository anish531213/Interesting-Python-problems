def sort(list1):
    pivot = list1[0]
    new_list = []
    for g in list1:
        k = [g]
        print(k)
        if g <= pivot:
            new_list = new_list + k
        else:
            new_list = k + new_list
        k.pop(0)
        print(k)
    return new_list

z = sort([1, -2, 6, 100, 5])
print (z)
