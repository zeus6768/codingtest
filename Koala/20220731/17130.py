import sys
input = sys.stdin.readline

def solve():
	n, m = map(int, input().split())

	island = []
	for i in range(n):
		isl = input().strip()
		if "R" in isl:
			r = isl.find("R")
			c = i
		island.append(isl)

	dp = [[0]*m for _ in range(n)]

	drc = [(1, 1), (0, 1), (-1, 1)]

	for j in range(m):
		for k in range(3):
			nr, nc = ...