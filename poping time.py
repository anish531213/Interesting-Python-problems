import time

def poping(l):
    start = time.time()
    l.pop(5)
    end = time.time()
    return (end-start)

z = poping([1, 2, 3, 4532, 5, 23])
print(z)
