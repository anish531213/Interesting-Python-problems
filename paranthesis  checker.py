from Stack import Stack

def par_checker(string):
    s = Stack()
    par_check = True
    i = 0
    while i < len(string) and par_check:
        if string[i] in '({[':
            s.push(string[i])
        elif string[i] == ')':
            if s.is_empty():
                par_check = False
            else:
                top = s.pop()
                if not matches(top, string[i]):
                    balanced = False
        i += 1
    if par_check and s.is_empty():
        return True
    else:
        return False

z = par_checker('{)')
print(z)
    
   
