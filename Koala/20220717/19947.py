def solve():
	H, Y = map(int, input().split())

	dp = [0] * (Y+5)
	dp[0] = H

	for i in range(1, Y+1):
		dp[i] = max(map(int, (dp[i-1]*1.05, dp[i-3]*1.2, dp[i-5]*1.35)))

	print(dp[Y])

solve()