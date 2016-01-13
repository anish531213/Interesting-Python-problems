def Arrange_array(arr):
    new_arr = sorted(arr)
    ans = []
    i = len(new_arr)-1
    j = 0
    k = 0
    while i > j:
        ans.append(new_arr[i])
        ans.append(new_arr[j])
        i -= 1
        j += 1
    if len(new_arr)%2 != 0:
        ans.append(new_arr[i])
    return ans

print(Arrange_array([1,2,3,4,5,7]))
