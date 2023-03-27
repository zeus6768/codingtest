from sys import stdin
from collections import deque

def input():
	return stdin.readline()

def solve():
	days = bfs(ripes)
	print(days) if is_all_ripe() else print(-1)

def bfs(xyz:list[tuple]):
	max_day = 0
	dxyz = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
	queue = deque([(*point, 0) for point in xyz])
	while queue:
		x, y, z, d = queue.popleft()
		for dx, dy, dz in dxyz:
			nx, ny, nz, nd = x+dx, y+dy, z+dz, d+1
			if 0<=nx<H and 0<=ny<N and 0<=nz<M and not TOMATOS[nx][ny][nz]:
				TOMATOS[nx][ny][nz] = 1
				queue.append((nx, ny, nz, nd))
				max_day = max(max_day, nd)
	return max_day

def is_all_ripe():
	for h in range(H):
		for n in range(N):
			for m in range(M):
				if not TOMATOS[h][n][m]:
					return False
	return True

def find_ripes():
	return [(h, n, m) for h in range(H) for n in range(N) for m in range(M) if TOMATOS[h][n][m]==1]

if __name__ == "__main__":
	M, N, H = map(int, input().split())
	TOMATOS = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
	if is_all_ripe():
		print(0)
		exit(0)
	ripes = find_ripes()
	solve()