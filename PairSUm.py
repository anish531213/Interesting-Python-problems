def PairSum(lst, S):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] == S-lst[j]:
                return True
    return False

z = PairSum([1, 3, 5], 8)
print(z)
