def invert_dictionary(d):
    inv = dict()
    for key in d:
        val = d[key]
        if val not in inv:
            inv[val] = [key]
        else:
            inv[val].append(key)
    return inv

z = invert_dictionary({'a': 1, 'p': 1, 'r': 2, 't': 1, 'o': 1})
print(z)
