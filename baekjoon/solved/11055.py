from copy import deepcopy

def solve():
	n = int(input())
	A = list(map(int, input().split()))
	dp = deepcopy(A)

	for i in range(1, n):
		for j in range(i):
			if A[j] < A[i] and dp[i] < dp[j]+A[i]:
				dp[i] = dp[j]+A[i]

	print(max(dp))
solve()