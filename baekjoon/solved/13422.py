import sys
input = sys.stdin.readline

def solve():

	T = int(input())

	for _ in range(T):

		N, M, K = map(int, input().split())
		town = [*map(int, input().split())]

		if N == M:
			if sum(town) < K:
				print(1)
			else:
				print(0)
			continue

		answer = 0
		
		cumulative_sum = [0]
		for i in range(0, N+M-1):
			c_sum = cumulative_sum[-1] + town[i%N]
			cumulative_sum.append(c_sum)

		for i in range(N):
			if cumulative_sum[i+M] - cumulative_sum[i] < K:
				answer += 1

		print(answer)

solve()