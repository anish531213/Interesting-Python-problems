from Stack import Stack

def par_checker(string):
    s = Stack()
    balanced = True
    i = 0
    while i < len(string) and balanced:
        if string[i] == '(':
            s.push(string[i])
        elif s.is_empty() == False:
            s.pop()
        else:
            balanced = False
        i += 1
    if balanced and s.is_empty():
        return "IT's valid"
    else:
        return "IT's not valid"

z = par_checker('(())(')
print(z)
    
