import sys

def input():
	return sys.stdin.readline()

def get_dp():
	dp = [0] * 101
	dp[0], dp[1], dp[2], dp[3], dp[4] = 1, 1, 1, 2, 2
	for i in range(5, 101):
		dp[i] = dp[i-1] + dp[i-5]
	return dp

if __name__ == "__main__":
	
	dp = get_dp()
	
	for _ in range(int(input())):
		N = int(input())
		print(dp[N-1])