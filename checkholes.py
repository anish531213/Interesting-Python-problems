def check_holes(string):
    i = 0
    for l in string:
        if l == 'a' or l == 'A' or l == 'b' or l == 'D' or l == 'd' or l == 'e' or l == 'g' or l == 'O' or l == 'o' or l == 'p' or l == 'P' or l == 'Q' or l == 'q' or l == 'R' :
            i += 1
        elif l == 'B':
            i += 2
    return i

z = check_holes('asdasfsdafasd')
print(z)
        
