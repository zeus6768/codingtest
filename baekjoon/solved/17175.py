n = int(input())

def superFibo(n):
	if n < 2:
		print(1)
	else:
		a, b = 1, 1
		for i in range(2, n+1):
			a, b = b, a+b+1
		print(b%1000000007)

superFibo(n)