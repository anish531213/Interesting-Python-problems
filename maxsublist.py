def MaxSublist(l):
    max_sum_so_far = 0
    current_sum_so_far = 0
    for i in range(len(l)):
        current_sum_so_far = max(current_sum_so_far + l[i], 0)
        max_sum_so_far = max(max_sum_so_far, current_sum_so_far)
    return max_sum_so_far

def MaxProfit(A):
    new = []
    for i in range(1, len(A)):
        new.append(A[i]-A[i-1])
    return MaxSublist(new)

print(MaxProfit([1, 3, -5, 4, -3, 17]))
