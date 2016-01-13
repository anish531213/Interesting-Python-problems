def StringCompression(string):
    start = string[0]
    count = 1
    compressed = ''
    for i in range(1, len(string)):
        if string[i] == start:
            count += 1
        else:
            compressed += start + str(count)
            start = string[i]
            count = 1
    return compressed

print(StringCompression('aabbcccdeee_'))
