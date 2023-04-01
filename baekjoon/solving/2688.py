def input():
	return __import__("sys").stdin.readline()

def solve(n):
	if n == 1:
		print(10)
		return
	for i in range(1, n):
		for j in range(10):
			dp[i][j] = sum(dp[i-1][:j+1])
	print(dp[n-1][-1])

if __name__ == "__main__":
	dp = [[0]*10 for _ in range(64)]
	dp[0] = list(range(1, 11))
	for _ in range(int(input())):
		n = int(input())
		solve(n)