# todo
# todo This solution is not finished.
# todo Come back in the future.
def eratosthenes():
	max_n = 40
	# Create a boolean array "prime[0..n]" and initialize
	# all entries it as true. A value in prime[i] will finally
	# be false if i is Not a prime, else true.
	prime_list = [True for _ in range(max_n + 1)]
	optimal = []
	p = 2
	while p * p <= max_n:
		# If prime[p] is not changed, then it is a prime
		if prime_list[p]:
			# Update all multiples of p
			for i in range(p * p, max_n + 1, p):
				prime_list[i] = False
		p += 1

	# Append all prime numbers
	for prime_index in range(2, max_n):
		if prime_list[prime_index]:
			optimal.append(prime_index)
			print(optimal)
	return optimal


if __name__ == '__main__':
	t = int(input().strip())
	x = eratosthenes()
	k_max = 0

	for a0 in range(t):
		numbers = []
		n = int(input().strip())
		product = 1
		for x_i in range(len(x)):
			p = x[x_i]
			if p <= n:
				for k in range(1, n+1):
					if p ** k < n:
						k_max = k
				print("Current p^k = {}^{} = {}".format(p, k_max, p ** k_max))
				print("Result: {} * {} = {}".format(product, p ** k_max, product * (p ** k_max)))
				product = product * (p ** k_max)
		print("{}".format(product))
