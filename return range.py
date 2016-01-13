def ReturnRange(arr, a, b):
    answer = ''
    for i in range(len(arr)-1):
        if arr[i] < a and arr[i+1] 
        if arr[i] > a and arr[i] < b and arr[i+1] < b:
            if arr[i+1] - arr[i] > 2:
                answer += str(arr[i]+1) + '-' + str(arr[i+1]-1) + ','
            elif arr[i+1] - arr[i] > 1:
                answer += str(arr[i]+1)+ ','
    return answer

l = [2, 5, 8, 10, 11, 12, 23, 25, 26, 100]
print(ReturnRange(l, 0, 50))
            
