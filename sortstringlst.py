def SortSringList(lst):
    for i in range(len(lst)):
        for j in range(i):
            if len(lst[j+1]) < len(lst[j]):
                lst[j+1], lst[j] = lst[j], lst[j+1]

lst = ['abcdf', 'a', 'arn']
SortSringList(lst)
print(lst)
