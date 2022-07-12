def solve():
	n = int(input())
	dp = [0] * (n+1)
	dp[1] = 1

	for i in range(2, n+1):
		_min = float('inf')
		j = 1
		while j**2 <= i:
			_min = min(_min, dp[i-j**2])
			j += 1
		dp[i] = _min+1
	
	print(dp[n])

solve()