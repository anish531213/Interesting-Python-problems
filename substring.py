def SubString(string, sub):
    i = 0
    while i < (len(string)-len(sub)+1):
        if string[i] == sub[0]:
            if string[i:(i+len(sub))] == sub:
                return True
        i += 1
    return False

print(SubString('anish', 'ht'))
