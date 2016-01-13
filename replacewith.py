def ReplaceWith(string, char):
    temp_list = string.split(' ')
    temp_str = char.join(temp_list)
    return temp_str


print(ReplaceWith('my name', '%20'))
