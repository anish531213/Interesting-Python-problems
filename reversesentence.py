def reverse_sentence(s):
    v = 0
    if s[len(s)-1] == '.':
        s = s[:len(s)-1]
        v = 1
    l = s.split(' ')
    l.reverse()
    new = ''
    for i in range(len(l)-1):
        new += l[i] + ' '
    if v == 1:
        new += l[len(l)-1] + '.'
    else:
        new += l[len(l)-1]
    return new

z = reverse_sentence('This is the real life or this is.')
print(z)
