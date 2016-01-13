def unique(word):
    for i in range(0, len(word), 1):
        for j in range(i+1, len(word), 1):
            if word[i] == word[j]:
                return False
    return True
z = unique('aanish')
print(z)
            
                   
                   
