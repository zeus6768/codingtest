import sys
input = sys.stdin.readline

def solve():
	n, m = map(int, input().split())
	V = [[*map(int, input().split())] for _ in range(m)]

	dp = [[0]*n for _ in range(m)]
	for i in range(m): dp[i][0] = V[i][0]

	for i in range(1, n):
		for j in range(m):
			list1 = []
			for k in range(m):
				if k == j:
					v = V[j][i]//2
				else:
					v = V[j][i]
				list1.append(dp[k][i-1] + v)
			dp[j][i] = max(list1)
	print(dp)

	answer = 0
	for i in range(m): answer = max(answer, dp[i][-1])

	print(answer)

solve()