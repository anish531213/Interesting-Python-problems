def BinarySearch(arr, num):
    start = 0
    end = len(arr)-1
    result1 = Findindex(arr, num, True)
    result2 = Findindex(arr, num, False)
    
    return result2-result1+1

def Findindex(arr, num, bol):
    start = 0
    end = len(arr)-1
    while start <= end:
        mid = (start+end)//2
        if arr[mid] < num :
            start = mid + 1
        elif arr[mid] > num:
            end = mid - 1
        else:
            result = mid
            if bol:
                end = mid - 1
            else:
                start = mid + 1
    return result

l = [1,1,1,2,2,2,2,3,3,3,5,5,9,9]
print(BinarySearch(l, 2))
