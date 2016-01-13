def is_pallindrome(string):
    if string == string[::-1]:
        return True
    return False

def find_that_number():
    for n in range(100000, 999999):
        if is_pallindrome(str(n%10000)) == True:
            n += 1
            if is_pallindrome(str(n%100000)) == True:
                n += 1
                if is_pallindrome(str(n%10000)) == True:
                    n += 1
                    if is_pallindrome(str(n)) == True:
                        return (n-4)
         
print(find_that_number())
    
