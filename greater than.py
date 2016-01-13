def greaterthan(l):
    new = []
    for i in range(len(l)):
        count = 0
        for j in range(i, len(l)):
            if l[i] < l[j]:
                count += 1
        new.append(count)
    return new

z = greaterthan([3, 4, 5, 9, 2, 1, 3])
print(z)

