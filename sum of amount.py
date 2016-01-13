def sum_of_amount(L, a):
	i = 0
	j = 0
	count = 0
	while i < len(L):
		sum = L[i]
		while j < len(L):
			sum += L[j]
			if sum == a:
				count += 1
			elif sum >  a:
				j += 1
				sum = L[i]
		i += 1
	return count
z = sum_of_amount([1, 2, 3], 4)
print(z)
