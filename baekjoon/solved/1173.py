def solve():
	N, m, M, T, R = map(int, input().split())
	x, workout, total = m, 0, 0
	while workout != N:
		if m + T > M:
			total = -1
			break
		elif x + T <= M:
			x += T
			workout += 1
		elif x - R < m:
			x = m
		else:
			x -= R
		total += 1
	print(total)

solve()