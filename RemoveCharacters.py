def Remove_gg(string):
    i = 0
    new = ''
    while i < len(string)-1:
        if string[i] == 'g':
            if string[i+1] == 'g':
                i += 1
            else:
                new += string[i]
        else:
            new += string[i]
        i += 1
    return new

print(Remove_gg('ggganigggshggg'+'`'))

