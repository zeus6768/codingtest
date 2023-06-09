import sys

def input():
	return sys.stdin.readline()

def solve():
	dp = [i for i in range(D+1)]

	for i in range(D+1):
		dp[i] = min(dp[i], dp[i-1] + 1)
		if shortcuts[i]:
			for e, d in shortcuts[i]:
				dp[e] = min(dp[e], dp[i] + d)
	
	print(dp[D])

N, D = map(int, input().split())
shortcuts = [[] for _ in range(D+1)]

for _ in range(N):
	s, e, d = map(int, input().split())
	if e <= D:
		shortcuts[s].append((e, d))

solve()