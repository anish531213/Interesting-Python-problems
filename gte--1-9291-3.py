def Get(a, l):
    new = ''
    for i in a:
        if i not in l:
            new += '_'
        else:
            new += i
    return new

print(Get('welcome', 'mel'))
