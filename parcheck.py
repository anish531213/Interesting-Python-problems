from Stack import Stack
def par_check(string):
    s = Stack()
    balanced = True
    i = 0 
    while i < len(string) and balanced:
        if string[i] == '(':
            s.push(string[i])
        else:
            if s.is_empty():
                balanced = False
            else:
                s.pop()
        i += 1
    if balanced and s.is_empty():
        return True
    else:
        return False

z = par_check('(())')
print(z)
            
