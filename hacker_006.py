def sum_one():
	return n*(n+1)/2


def sum_two():
	return n*(n+1)*(2*n+1)/6


if __name__ == '__main__':
	t = int(input().strip())
	for a0 in range(t):
		n = int(input().strip())
		summary = [sum_one(),sum_two()]
		result = summary[0] ** 2 - summary[1]
		print(int(result))