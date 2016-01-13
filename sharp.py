def sharp(n):
    if n== 1:
        return 1
    elif n==0:
        return 0
    elif n==2:
        return 2
    else:
        return (sharp(n-1) ** n)
z = sharp(4)
print(z)
