# 내 풀이
def solution():
	n = int(input())
	dp = [float('inf')] * (n+1)
	dp[1], dp[2], dp[3] = 0, 1, 1
	if n < 4:
		print(dp[n])
	else:
		for i in range(4, n+1):
			if (i%3==0) and (i%2==0):
				dp[i] = min(dp[i//3], dp[i//2], dp[i-1]) + 1
			elif i%3==0:
				dp[i] = min(dp[i//3], dp[i-1]) + 1
			elif i%2==0:
				dp[i] = min(dp[i//2], dp[i-1]) + 1
			else:
				dp[i] = dp[i-1] + 1
		print(dp[n])

solution()

# 코알라 풀이
def solution2():
	n = int(input())
	dp = [float('inf')] * (n+1)
	dp[n] = 0
	for i in range(n, 0, -1):
		if i % 3 == 0:
			dp[i//3] = min(dp[i//3], dp[i]+1)
		if i % 2 == 0:
			dp[i//2] = min(dp[i//2], dp[i]+1)
		dp[i-1] = min(dp[i-1], dp[i]+1)
	print(dp[1])

solution2()