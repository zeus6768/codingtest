
def solve():
	n, m = map(int, input().split())
	breaks = [*map(int, input().split())]

	available = [False if i in breaks else True for i in range(0, n+1)]
	dp = [0] * (n+6)
	dp[1], dp[3], dp[5] = 10000, 25000, 37000

	for i in range(1, n+1):
		dp[i]
		...

solve()

