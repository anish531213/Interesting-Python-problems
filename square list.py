def square(sorted_list):
    new_list = []
    for elements in sorted_list:
        new_list.append(elements ** 2)
    return new_list
z = square([1, 2, 6,5])
z = sorted(z)
print(z)
