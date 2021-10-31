import sys
read = sys.stdin.readline
N = int(read())
A = list(map(int, read().split()))
dp = []
for i in range(len(A)):
	if i == 0:
		dp.append(1)
	elif A[i-1] < A[i]:
		dp.append(dp[i-1] + 1)
	else:
		dp.append(dp[i-1])

print(max(dp))


# 10 30 20 25 27 50
#  1  2  2 2+1