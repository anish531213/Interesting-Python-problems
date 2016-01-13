def RemoveSub(string, sub):
    i = 0
    new = ''
    while i < len(string):
        if string[i] == sub[0]:
            if string[i : (i+len(sub))] == sub:
                i += len(sub)
            else:
                new += string[i]
                i += 1
        else:
            new += string[i]
            i += 1
    return new

print(RemoveSub('ggcdfgggdkgg', 'gg'))