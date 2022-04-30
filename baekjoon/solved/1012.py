import sys
from collections import deque
input = sys.stdin.readline

def solution():
	t = int(input())
	for _ in range(t):
		m, n, k = map(int, input().split())

		farm = [[0] * m for _ in range(n)]
		for _ in range(k):
			x, y = map(int, input().split())
			farm[y][x] = 1

		worms = 0
		for i in range(n):
			for j in range(m):
				if farm[i][j]:
					bfs(farm, i, j)
					worms += 1

		print(worms)
	
def bfs(graph, i, j):
	dx = (0, 0, 1, -1)
	dy = (1, -1, 0, 0)
	graph[i][j] = 0
	queue = deque([(i, j)])
	while queue:
		v = queue.popleft()
		for k in range(4):
			nx, ny = v[0]+dx[k], v[1]+dy[k]
			if 0 <= nx < len(graph) and 0 <= ny < len(graph[i]) and graph[nx][ny] == 1:
				graph[nx][ny] = 0
				queue.append((nx, ny))

solution()
	
