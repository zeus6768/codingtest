def solve():
	s1 = input()
	s2 = input()
	l1, l2 = len(s1), len(s2)

	dp = [[0]*(l2+1) for _ in range(l1+1)]

	_max = 0

	for i in range(l1):
		for j in range(l2):
			if s1[i] == s2[j]:
				dp[i+1][j+1] = dp[i][j] + 1
				_max = max(_max, dp[i+1][j+1])

	print(_max)


solve()