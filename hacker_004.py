that_list = []
for one in range(100, 1000):
	for two in range(100, 1000):
		product = one * two
		if str(product) == str(product)[::-1] and product not in that_list:
			that_list.append(product)
that_list.sort()


if __name__ == '__main__':
	n = int(input())
	for _ in range(n):
		a = int(input())
		for i in range(len(that_list) - 1, -1, -1):
			if that_list[i] < a:
				print(that_list[i])
				break