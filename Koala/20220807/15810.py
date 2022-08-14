def solve():
	n, m = map(int, input().split())
	A = [*map(int, input().split())]

	l, r = 0, 10**12
	answer = 1_000_000

	while l <= r:
		mid = (l+r) // 2
		
		ball = 0
		for a in A:
			ball += mid//a

		if ball < m:
			l = mid + 1
		else:
			r = mid - 1
			answer = mid

	print(answer)

solve()