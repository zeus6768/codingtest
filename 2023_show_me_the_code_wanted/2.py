from collections import deque

def bfs(x, y):
	q = deque([(x, y)])
	visited[x][y] = True
	while q:
		r, c = q.popleft()
		for dr, dc in D:
			nr, nc = (r + dr) % N, (c + dc) % M
			if graph[nr][nc] == 0 and not visited[nr][nc]:
				q.append((nr, nc))
				visited[nr][nc] = True

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]
D = ((1, 0), (-1, 0), (0, -1), (0, 1))

answer = 0
for i in range(N):
	for j in range(M):
		if graph[i][j] == 0 and not visited[i][j]:
			bfs(i, j)
			answer += 1

print(answer)