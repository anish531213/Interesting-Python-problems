def common_substring(s1, s2):
    i = 0
    list1 = []
    while i < len(s1):
        j = 0
        new = ''
        while j < len(s2):
            if s2[j] == s1[i]:
                new += s2[j]
                i += 1
                j += 1
                list1.append(new)
            else:
                j += 1
        i += 1
    return list1

z = common_substring('coazz', 'cozazz')
print(z)
