def reverse(n):
    n = str(n)
    n = n[::-1]
    n = int(n)
    return(n)

   
def find_age():
    m = 0
    z = 0
    for n in range(36, 120):
        if (n - 36) == reverse(n):
            print(n)
            z += 1

print(find_age())

