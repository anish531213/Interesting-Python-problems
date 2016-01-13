def reverse_pair(l):
    new_list = []
    for i in range(0, len(l)):
        for j in range(i+1, len(l)):
            if l[i] == (l[j])[::-1]:
                new_list.append(l[i])
                new_list.append(l[j])
    return new_list
    
z = reverse_pair(['anish', 'hsina', 'anis'])
print(z)
