def GetInside(word):
    
    new_word = word[1:(len(word)-1)]
    return new_word

answer = GetInside('trips')
print('GetInside #1: expected "rip", got', answer)
answer = GetInside('so')
print('GetInside #2: expected an empty string, got', answer)

