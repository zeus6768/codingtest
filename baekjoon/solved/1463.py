def solve():
	x = int(input())
	dp = [float('inf')] * 1000001
	dp[1], dp[2], dp[3] = 0, 1, 1
	if x < 4:
		print(dp[x])
	else:
		for i in range(4, x+1):
			if (i%3==0) and (i%2==0):
				dp[i] = min(dp[i//3], dp[i//2], dp[i-1]) + 1
			elif i%3==0:
				dp[i] = min(dp[i//3], dp[i-1]) + 1
			elif i%2==0:
				dp[i] = min(dp[i//2], dp[i-1]) + 1
			else:
				dp[i] = dp[i-1] + 1
		print(dp[x])
solve()