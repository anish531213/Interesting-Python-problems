
def histogram(s):
    d = dict()
    for c in s:
        z = d.get(c, 0)
        z += 1
        d[c] = z
    return d

h = histogram('anishadhikari')

def print_hist(h):
    for c in h:
        print(c, h[c])

print_hist(h)
