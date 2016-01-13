
def max_profit(l):
    new = []
    for i in range(1,len(l)):
        new.append(l[i]-l[i-1])
    return max_sum(new)

def max_sum(arr):
    temp_sum = 0
    sumn = 0
    for i in arr:
        temp_sum += i
        temp_sum = max(temp_sum, 0)
        sumn = max(sumn, temp_sum)
    return sumn

print(max_profit([5, 2, 3, 4, 9, 1, 6, 2]))
