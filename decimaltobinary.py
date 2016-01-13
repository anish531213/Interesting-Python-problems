def decimaltobinary(d):
    b = ''
    while d != 0:
        b += (str(d%2))
        d = d // 2

    return b[::-1]

z = decimaltobinary(5)
print(z)

def binarytodecimal(b):
    d = 0
    for i in range(len(b)) :
        d += (2**i)*int(b[len(b)-1-i])
    return d

k = binarytodecimal('111')
print(k)
