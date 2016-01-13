# 1 1 3 2 4 2 1 1
def peak_finder(l):
    if l[0] >= l[1]:
        print("peak ", l[0])
    for i in range(1, len(l)-1):
        if l[i] >= l[i-1] and l[i] >= l[i+1]:
            print("peak ", l[i])
    if l[len(l)-1] >= l[len(l)-2]:
        print("peak ", l[len(l)-1])

peak_finder([1, 1, 3, 2, 4, 2, 1, 1])

