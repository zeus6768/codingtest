def factorial(n):
	for i in range(n-1, 1, -1):
		n *= i
	return n if n else 1

def combination(n, m):
	return factorial(n) // factorial(n-m) // factorial(m)

if __name__ == "__main__":
	n, m = map(int, input().split())
	print(combination(n, m))