def Sum_of_multiples(n):
    sum = 0
    i = 0
    while i < n:
        if i % 3 == 0 or i % 5 == 0:
            sum += i
        i += 1
    return sum

print(Sum_of_multiples(1000))
