def LongestPallindrome(string):
    long = ''
    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            temp = string[i:j]
            if temp == temp[::-1]:
                if len(temp) > len(long):
                    long = temp
    return long

print(LongestPallindrome('surarjaaj'))
                
