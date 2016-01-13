def IsPrime(n):
	m = 2
	while m < n:
		if n%m == 0:
			return False
		return True
		
answer = IsPrime(12)
print('IsPrime: expected True, got', answer)
