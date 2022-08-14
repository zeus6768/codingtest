def solve():
	s1 = input()
	s2 = input()
	l1, l2 = len(s1), len(s2)

	dp1 = [[0]*(l2+1) for _ in range(l1+1)]
	dp2 = [['']*(l2+1) for _ in range(l1+1)]

	for i in range(1, l1+1):
		for j in range(1, l2+1):
			if s1[i-1]==s2[j-1]:
				dp1[i][j] = dp1[i-1][j-1] + 1
				dp2[i][j] = dp2[i-1][j-1] + s1[i-1]
			else:
				if dp1[i-1][j] < dp1[i][j-1]:
					dp1[i][j] = dp1[i][j-1]
					dp2[i][j] = dp2[i][j-1]
				else:
					dp1[i][j] = dp1[i-1][j]
					dp2[i][j] = dp2[i-1][j]

	print(dp1[-1][-1])
	print(dp2[-1][-1]) if dp1[-1][-1] else None

solve()