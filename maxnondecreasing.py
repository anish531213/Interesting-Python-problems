def MaxNonDecreasing(l):
    maxx = [l[0]]
    temp = [l[0]]
    for i in range(1, len(l)):
        if l[i] > l[i-1]:
            temp.append(l[i])
        else:
            temp = [l[i]]
        if len(temp) > len(maxx):
                maxx = temp
    return maxx

print(MaxNonDecreasing([1, 3, 4, 1, 5, 8, 9]))
            
        
