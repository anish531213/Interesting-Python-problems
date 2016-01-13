def BalancingIndex(l):
    sumn = sum(l)
    div = 0
    temp_sum = 0
    new_lst = []
    for i in range(1, len(l)):
        temp_sum += l[i-1]
        div = (sumn-l[i])/2
        if temp_sum == div:
            return i
        else:
            new_lst.append(abs(div-temp_sum))
    return min(new_lst)

print(BalancingIndex([1, 2, 3, 2, 1, 5, 2, 1]))
