def solve():
	count = 0
	is_prime = [True] * (N+1)
	for i in range(2, N+1):
		for j in range(i, N+1, i):
			if is_prime[j]:
				is_prime[j] = False
				count += 1
				if count == K:
					print(j)
					return

N, K = map(int, input().split())
solve()
