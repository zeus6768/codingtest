def solution():
	n = int(input())
	group = [[*map(int, input().split())] for _ in range(n)]
	rank = [1] * n
	for i, one in enumerate(group):
		for _, other in enumerate(group):
			if one[0] < other[0] and one[1] < other[1]:
				rank[i] += 1
	print(*rank)

solution()