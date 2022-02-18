from itertools import permutations

n, m = map(int, input().split())
items = list(permutations(range(1, n+1), m))
for item in items:
	[print(i, end=' ') for i in item]
	print()

