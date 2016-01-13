def sum_without_int(s1, s2):
    int_s1 = 0
    int_s2 = 0
    for i in range(len(s1)):
        int_s1 += int(s1[i])* (10 **(len(s1)-1-i))
    for j in range(len(s2)):
        int_s2 += int(s2[j])* (10 **(len(s2)-1-j))
    return (int_s1 + int_s2)

z  = sum_without_int('34', '34')
print(z)
