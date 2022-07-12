def solve():
	n = int(input())
	a, b = 0, 1
	if n <= 1:
		print(n)
		return
	for _ in range(1, n):
		a, b = b, (a+b)%1000000007
	print(b)
solve()