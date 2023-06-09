import sys
sys.setrecursionlimit(10**5)

def input():
	return sys.stdin.readline().strip()

def dfs(visited, x, y):
	visited[x][y] = True
	for dx, dy in dxy:
		nx, ny = x+dx, y+dy
		if 0<=nx<H and 0<=ny<W and sheeps[nx][ny] == '#' and not visited[nx][ny]:
			dfs(visited, nx, ny)

dxy = ((1, 0), (-1, 0), (0, 1), (0, -1))

T = int(input())

for _ in range(T):

	H, W = map(int, input().split())
	sheeps = tuple(input() for _ in range(H))
	visited = [[False]*W for _ in range(H)]
	answer = 0

	for i in range(H):
		for j in range(W):
			if sheeps[i][j] == '#' and not visited[i][j]:
				dfs(visited, i, j)
				answer += 1
	
	print(answer)