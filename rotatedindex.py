def RotatedIndex(arr):
    start = 0
    end = len(arr)-1
    while start < end:
        mid = (start+end)//2
        if arr[mid] < arr[mid+1] and arr[mid] < arr[mid-1]:
            return mid
        if arr[mid] > arr[end]:
            start = mid + 1
        else:
            end = mid - 1

l = [7, 8, 9, 10 ,11, 13, 6, 7]
print(RotatedIndex(l))
