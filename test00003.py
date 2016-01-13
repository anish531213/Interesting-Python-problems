def is_pallindrome(word):
    if word == word[::-1]:
        return True
    return False

print(is_pallindrome('nsadsa'))
