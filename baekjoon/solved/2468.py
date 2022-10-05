import sys
input = sys.stdin.readline

def solution():
	n = int(input())
	graph = [[*map(int, input().split())] for _ in range(n)]
	visited = [[False] * n for _ in range(n)]
	count = 0
	
	def dfs(r, c, v):
		d = ((-1, 0), (0, 1), (1, 0), (0, -1))
		stack = [(r, c)]
		while stack:
			x, y = stack.pop()
			if not visited[x][y] and graph[x][y] > v:
				visited[x][y] = True
				for i in range(4):
					nr = x + d[i][0]
					nc = y + d[i][1]
					if (0 <= nr < n) and (0 <= nc < n) and (not visited[nr][nc]) and (graph[nr][nc] > v):
						stack.append((nr, nc))

	for v in range(101):
		visited = [[False] * n for _ in range(n)]
		tmp = 0 
		for i in range(n):
			for j in range(n):
				if not visited[i][j] and graph[i][j] > v:
					tmp += 1
					dfs(i, j, v)
		count = max(count, tmp)

	print(count)

solution()