from math import factorial

def binomial(n, k):
	return factorial(n) // (factorial(k)*factorial(n-k))

def solve():
	n, k = map(int, input().split())
	r = binomial(n, k) % 10007
	print(r)

solve()