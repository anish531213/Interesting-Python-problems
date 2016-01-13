def PrintDuplicate(string):
    dict_of_chars = {}
    # i is my evry character of the string 
    for i in string:
        temp = dict_of_chars.get(i, 0)
        temp += 1
        dict_of_chars[i] = temp
    for key in dict_of_chars:
        if dict_of_chars[key] > 1:
            print (key)

PrintDuplicate('Java')
