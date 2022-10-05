def solve():
	N, M, K = map(int, input().split())
	A = [*map(int, input().split())]
	B = [*map(int, input().split())]

	answer = 0
	for a in A:
		for b in B:
			if a ^ b < K:
				answer += 1

	print(answer)

solve()