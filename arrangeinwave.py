def ArrangeWave(lst):
    lst.sort()
    for i in range(0, len(lst)-1, 2):
        lst[i], lst[i+1] = lst[i+1], lst[i]

lst = [3, 5, 7, 9, 10, 13]
ArrangeWave(lst)
print(lst)
