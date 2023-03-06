def main():
	
	N, K = map(int, input().split())

	dp = [float('inf')] * 46
	dp[N] = 0

	for x in range(1, N+1):
		dp[N-x] = dp[N-x+1] + 1

	for _ in range(2):
		for x in range(N, K+2):
			if x % 2 == 0:
				dp[x] = min(dp[x], dp[x-1]+1, dp[x+1]+1, dp[x//2]+1)
			else:
				dp[x] = min(dp[x], dp[x-1]+1, dp[x+1]+1)

	print(dp[K])

main()

"""
3 4 5 10 20 21 42 43

3 6 12 11 22 44 43


"""