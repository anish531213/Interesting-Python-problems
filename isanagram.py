def is_anagram(l, s):
    i = 0
    while i < len(l):
        if l[i] in s:
            i += 1
            continue
        else:
            return False
    return True

z = is_anagram('anish', 'nzshi')
print(z)
            
