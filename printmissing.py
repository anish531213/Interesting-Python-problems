def print_missing(l):
    sumn = (1 + l[len(l)-1]) * l[len(l)-1] * (0.5)
    x  = 0
    for i in l:
        x += i
    return (sumn - x)

z = print_missing([0, 1, 2, 3, 4, 5, 7])
print(int(z))
