def gg_remove(word):
    index = 0
    new_word = ''
    while index<len(word):
        if (word[index] + word[index+1]) == 'gg':
            index += 2
        else:
            new_word += word[index]
            index += 1
        if index > 0:
            break
    return new_word

z = gg_remove('hjkjkjgggg')
print(z)
