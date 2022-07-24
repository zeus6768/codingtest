import sys
input = sys.stdin.readline

def solve():
	n = int(input())
	food = [int(input()) for _ in range(n)]

	dp = [0]*(n+1)
	dp[0], dp[1] = food[0], food[0]+food[1]//2

	for i in range(2, n):
		dp[i] = max(dp[i-2]+food[i], dp[i-1]+food[i])

