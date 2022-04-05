def solve():
	n, k = [int(i) for i in input().split()]
	nu, de = 1, 1
	while k:
		nu *= n
		de *= k
		n -= 1
		k -= 1
	print(nu//de)
	
solve()