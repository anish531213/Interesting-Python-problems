def ValidShuffle(first, second, third):
    i = 0
    j = 0
    k = 0
    check = False
    while k < len(third):
        if i < len(first) and j < len(second):
            if third[k] == first[i]:
                check = True
                i += 1
            elif third[k] == second[j]:
                check = True
                j += 1
            else:
                check = False
                break
        elif i < len(first):
            if third[k] == first[i]:
                check = True
                i += 1
            else:
                check = False
                break
        else:
            if third[k] == second[j]:
                check = True
                j += 1
            else:
                check = False
                break
        k += 1
    return check

print(ValidShuffle('a', '', 'a'))
