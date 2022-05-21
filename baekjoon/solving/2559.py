def solution():
	N, K = map(int, input().split())
	numbers = [*map(int, input().split())]
	current = sum(numbers[:K])
	result = current
	for i in range(N-K):
		current -= numbers[i]
		current += numbers[i+K]
		if result < current:
			result = current
	print(result)

solution()