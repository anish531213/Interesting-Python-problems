def FindSub(string, element):
    sub = []
    for i in range(0, len(string)):
        d = {}
        for k in element:
            d[k] = d.get(k, 0) + 1
        count = 0
        tmp = ''
        for j in range(i, len(string)):
            if string[j] in d:
                tmp += string[j]
                d[string[j]] -= 1
                if d[string[j]] >= 0:
                    count += 1
            else:
                if tmp != '':
                    tmp += string[j]
            if count == len(element):
                sub.append(tmp)
                break
            print (tmp)
    return sub

print(FindSub('adobecodebanc', 'abc'))
