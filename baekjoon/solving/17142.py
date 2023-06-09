from itertools import combinations as cb
from collections import deque
import sys

def input() -> str:
	return sys.stdin.readline()

def is_bound(x:int, y:int) -> bool:
	return 0<=x<N and 0<=y<N

def bfs(start: tuple) -> int:
	time = 0
	lab_time[start[0]][start[1]] = 0
	visited = [[False]*N for _ in range(N)]
	visited[start[0]][start[1]] = True
	queue = deque([start])
	while queue:
		x, y = queue.popleft()
		for dx, dy in DXY:
			nx = x + dx
			ny = y + dy
			if is_bound(nx, ny) and not visited[nx][ny] and lab[nx][ny] != TYPE["wall"]:
				visited[nx][ny] = True
				lab_time[nx][ny] = min(lab_time[nx][ny], lab_time[x][y]+1)
				queue.append((nx, ny))
				if lab[nx][ny] == TYPE["empty"]:
					time = max(time, lab[nx][ny])
	return time

def check(lab_time):
	for i in range(N):
		for j in range(N):
			if (lab[i][j] == TYPE["empty"] and lab_time[i][j] == float("inf")):
				return False
	return True

def solve() -> None:
	global answer, lab_time
	for indices in virus_indices:
		lab_time = [[float("inf")]*N for _ in range(N)]
		for i in range(M):
			r = bfs(virus_xy[indices[i]])
			answer = min(answer, r)
	print(answer) if answer != 2**31 else print(-1)


TYPE = {"empty": 0, "wall": 1, "virus": 2}
DXY = ((1, 0), (-1, 0), (0, 1), (0, -1))

if __name__ == "__main__":
	N, M = map(int, input().split())
	lab = list()
	lab_time = list()

	virus_xy = list()
	virus_indices = list()

	for i in range(N):
		lab.append(tuple(map(int, input().split())))
		[virus_xy.append((i, j)) for j in range(N) if lab[i][j] == 2]

	virus_count = len(virus_xy)
	virus_indices = tuple(cb(range(virus_count), M))

	answer = 2**31

	solve()