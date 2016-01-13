def GetReverse(word):
    n = len(word) - 1
    z = ''
    while n >= 0:
        z += word[n]
        n -= 1
    return z
    
answer = GetReverse('banana')
print('GetReverse: expected "ananab", got', answer)

