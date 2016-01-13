
def sum_target(A, target):
    for i in range(len(A)):
        k = 0
        for j in range(i, len(A)):
            k += A[j]
            if k == target:
                return A[i:j+1]
    return("no consecutive sum found")

z = sum_target([1, 2, 3, 5, 7], 12)
print(z)

def sumoftarget(A, target):
    start = 0
    end = 0
    sumn = A[0]
    if sumn == target:
        return True
    while end < len(A):
        if sumn > target:
            sumn -= A[start]
        else:
            end += 1
            if end < len(A):
                sumn += A[end]
        if sumn == target:
            return True
    return False

z = sumoftarget([1, 2, 3, 7, 1], 5)
print(z)
      
