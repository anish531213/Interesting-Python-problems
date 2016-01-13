def GreedyAlgorithm(amount):
    change = [100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.10, 0.05, 0.01]
    cashed = []
    i = 0
    while amount > 0:
        if amount >= change[i]:
            amount -= change[i]
            amount = round(amount, 2)
            cashed.append(change[i])
        else:
            i += 1
    return cashed

print(GreedyAlgorithm(232.32))
