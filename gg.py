def gg_removed(word):
    index = 0
    kate = 0
    new_word = ''
    while index < (len(word)-1):
        if (word[index]+word[index+1]) == 'gg':
            index += 2
        else:
            new_word += word[index]
            index += 1
        
    return(new_word + word[len(word)-1])

z = gg_removed('sanggg')
print(z)
