def list_sum(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + list_sum(num_list[1:])

z = list_sum([1, 2, 5, 9, 13])
print(z)
