def max_profit(l):
    m = 0
    for i in range(len(l)):
        for j in range(i, len(l)):
            if l[j]-l[i] > m:
                m = l[j]-l[i]
    return m

z = max_profit([6, 5, 4, 5, 3])
print(z)

#new method


        
