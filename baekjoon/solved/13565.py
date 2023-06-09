import sys
sys.setrecursionlimit(10**6)

M, N = map(int, input().split())
fiber = tuple(input() for _ in range(M))
dxy = ((1, 0), (-1, 0), (0, 1), (0, -1))
visited = [[False]*N for _ in range(M)]

def dfs(x, y):
	if x == M-1:
		print("YES")
		exit(0)
	visited[x][y] = True
	for dx, dy in dxy:
		nx, ny = x + dx, y + dy
		if 0<=nx<M and 0<=ny<N and fiber[nx][ny]=='0' and not visited[nx][ny]:
			dfs(nx, ny)

for i in range(N):
	dfs(0, i)

print("NO")