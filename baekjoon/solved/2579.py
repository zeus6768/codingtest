import sys
input = sys.stdin.readline

def solve():
	n = int(input())
	stairs = [int(input()) for _ in range(n)]
	
	dp = [[0] * (n+1) for _ in range(2)]
	dp[0][0], dp[1][0] = 0, 0
	dp[0][1], dp[1][1] = stairs[0], stairs[0]

	for i in range(1, n):
		dp[0][i+1] = dp[1][i] + stairs[i]
		dp[1][i+1] = max(dp[0][i-1], dp[1][i-1]) + stairs[i]

	print(max(dp[0][-1], dp[1][-1]))

solve()