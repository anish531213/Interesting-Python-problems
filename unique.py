def unique(word):
    n = 0
    y = word
    for x in word:
        k = y[:n]+ y[(n+1):]
        for z in k:
            if x == z:
                return False
        n += 1
    return True
z = unique('aaish')
print(z)
