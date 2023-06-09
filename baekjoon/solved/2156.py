import sys

def input():
	return sys.stdin.readline()

def solve():
	dp = [0]*(N+1)
	dp[0] = wines[0]
	for i in range(1, N):
		dp[i] = max(dp[i-1], dp[i-2]+wines[i], dp[i-3]+wines[i-1]+wines[i])
	answer = max(dp)
	print(answer)

if __name__ == "__main__":
	N = int(input())
	wines = [int(input()) for _ in range(N)]
	solve()