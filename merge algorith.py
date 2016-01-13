def Merge(l1, l2):
    i = 0
    j = 0
    new = []
    while i < len(l1) and j < len(l2):
        if l1[i]< l2[j]:
            new.append(l1[i])
            i += 1
        else:
            new.append(l2[j])
            j += 1
    while i < len(l1):
        new.append(l1[i])
        i += 1
    while j < len(l2):
        new.append(l2[j])
        j += 1
    return new

print(Merge([1, 2, 7], [3, 4, 9]))
