def is_reverse(x, y):
    j = len(y)-1
    for i in range(0, len(x), 1):
        if x[i] == y[j]:
            j -= 1
            return True
        else:
            return False
            break
    


x = input("enter first string")
y = input("enter second string")
reverse = is_reverse(x, y)
print(reverse)
