def solve():
	for coin in coins:
		for i in range(coin, k+1):
			dp[i] += dp[i-coin]

if __name__ == "__main__":
	n, k = map(int, input().split())
	coins = [int(input()) for _ in range(n)]
	dp = [0] * (k+1)
	dp[0] = 1
	solve()

"""         0  1  2  3  4  5  6  7  8  9  10
coin == 1: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
coin == 2: [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6]
coin == 5: [1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 10]

"""