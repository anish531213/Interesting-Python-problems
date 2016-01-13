def expandAroundCentre(string, i, j):
    while string[i] == string[j] and i >= 0 and j < len(string):
        i -= 1
        j += 1
    return string[i+1:j]
        
def LongestPallindrome(string):
    longest = string[0]
    for i in range(1, len(string)-1):
        string1 = expandAroundCentre(string, i, i)
        if len(string1) > len(longest):
            longest = string1
        string2 = expandAroundCentre(string, i, i+1)
        if len(string2) > len(longest):
            longest = string2
    return longest
print(LongestPallindrome('abaca'))        
