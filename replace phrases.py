def ConvertString(s, t, w):
    new = ''
    i = 0
    while i < len(s):
        if s[i] == t[0]:
            if s[i:i+len(t)] == t:
                new += w
                i += len(t)
            else:
                new += s[i]
                i += 1
        else:
            new += s[i]
            i += 1
    return new

print(ConvertString('dadda', 'ad', 's'))
    
