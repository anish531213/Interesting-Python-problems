def CountVowels(string):
    sets = {'a', 'e', 'i', 'o', 'u'}
    no_of_vowels = 0
    no_of_consonents = 0
    for i in string:
        if i in sets:
            no_of_vowels += 1
        else:
            no_of_consonents += 1
    print("The number of vowels is %i and number of consonents is %d" %(no_of_vowels, no_of_consonents))
    
CountVowels('anish')
