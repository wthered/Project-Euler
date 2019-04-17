t = int(input().strip())
for a0 in range(t):
	n = int(input().strip())
	summation = 0
	for i in range(1, n):
		if i % 3 is 0 or i % 5 is 0:
			summation += i
	print(summation)
