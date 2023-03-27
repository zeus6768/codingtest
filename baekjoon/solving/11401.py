def numerator(n, k):
	r = 1
	for i in range(n, n-k, -1):
		r = r*i%M
	return r

def factorial(n):
	r = 1
	for i in range(n, 1, -1):
		r = r*i%M
	return r

def modular_exp(x, n):
	y, u = 1, x % M
	while n > 0:
		if n % 2:
			y = (y*u) % M
		n //= 2
		u = (u**2) % M
	return y

if __name__ == "__main__":
	N, K = map(int, input().split())
	M = 1_000_000_007
	A = numerator(N, K)
	B = modular_exp(factorial(K), M-2)
	answer = A*B%M
	print(answer)