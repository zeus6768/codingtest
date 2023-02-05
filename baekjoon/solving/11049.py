def solve():

	N = int(input())
	matrices = [tuple(map(int, input().split())) for _ in range(N)]

	dp = [[0]*N for _ in range(N)]

	for i in range(1, N):
		for j in range()


def operation_count(size1, size2):
	if size1[1] != size2[0]:
		raise ValueError
	return size1[0] * size2[0] * size2[1]


