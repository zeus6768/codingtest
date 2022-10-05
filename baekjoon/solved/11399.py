def solve():
	n = int(input())
	P = sorted(map(int, input().split()))

	cumulative_sum = [0]
	for i in range(n):
		prev = cumulative_sum[-1]
		now = P[i]
		cumulative_sum.append(prev + now)

	answer = sum(cumulative_sum)

	print(answer)

solve()