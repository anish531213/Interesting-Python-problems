def SentRev(s):
    z = None
    new = ''
    ans = ''
    if s[len(s)-1] == '.':
        s = s[:len(s)-1]
        z = True
    for i in s:
        if i != ' ':
            new += i
        else:
            ans = new + ' ' + ans
            new = ''
    ans = new + ' ' + ans
    if z:
        ans = ans[:len(ans)-1] + '.'
    return ans

print(SentRev('my name is Anish'))
            
        
        
