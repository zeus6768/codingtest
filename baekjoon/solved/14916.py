import time

# 조건문 풀이
def solution1():
	n = int(input())
	q, r = n // 5, n % 5

	if q:
		if r:
			if r % 2: 
				print((q-1)+((r+5)//2))
			else:
				print(q+(r//2))
		else:
			print(q)
	else:
		if r == 1 or r == 3:
			print(-1)
		else:
			print(r // 2)

# DP를 사용한 풀이
def solution2():
	n = int(input())
	dp = [float('inf')] * 100001
	dp[2], dp[4], dp[5] = 1, 2, 1
	for i in range(6, n+1):
		dp[i] = min(dp[i-2], dp[i-5]) + 1
	if dp[n] == float('inf'):
		print(-1)
	else:
		print(dp[n])

solution2()