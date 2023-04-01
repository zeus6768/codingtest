from collections import deque
from sys import stdin

def input():
	return stdin.readline()

def rotate(x, d, k):
	for i in range(x-1, N, x):
		if d == 0:
			plates[i].rotate(k)
		if d == 1:
			plates[i].rotate(-k)
	# adjacents = findall_adjacent_same()
	# if adjacents:
	# 	for i, j in adjacents:
	# 		plates[i][j] = 0
	# else:
	# 	average()

def findall_adjacent_same() -> list[tuple]:
	adjacents = list()
	for i in range(N):
		for j in range(M):
			adjacents.extend(find_adjacent_same(i, j))
	return adjacents

def find_adjacent_same(i, j):
	return [(x, y) for x, y in ((i, (j-1)%M), (i, (j+1)%M), (i-1, j), (i+1, j)) if 0<=x<N and 0<=y<M and not deleted[i][j]]

def average():
	avg = get_average()
	for i in range(N):
		for j in range(M):
			if avg < plates[i][j]:
				plates[i][j] -= 1
			if avg > plates[i][j]:
				plates[i][j] += 1

def get_average():
	count, total = 0, 0
	for i in range(N):
		for j in range(M):
			if not deleted[i][j]:
				count += 1
				total += plates[i][j]
	return total / count

def print_result():
	print(sum(plates[i][j] for i in range(N) for j in range(M) if not deleted[i][j]))

def log(msg=""):
	print(msg)
	pr = [[plates[i][j] if not deleted[i][j] else 0 for j in range(M)] for i in range(N)]
	[print(p) for p in pr]

if __name__ == "__main__":
	N, M, T = map(int, input().split())
	plates = [deque(map(int, input().split())) for _ in range(N)]
	deleted = [[False]*M for _ in range(N)]
	log("\nplates")
	for _ in range(T):
		x, d, k = map(int, input().split())
		rotate(x, d, k)
	print_result()