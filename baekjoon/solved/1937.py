import sys
sys.setrecursionlimit(10**6)

def input():
	return sys.stdin.readline()

def solve():
	answer = 0
	for i in range(n):
		for j in range(n):
			if not routes[i][j]:
				answer = max(answer, dfs(i, j))
	print(answer)

def dfs(r, c):
	if routes[r][c]:
		return routes[r][c]
	routes[r][c] = 1
	for dr, dc in drc:
		nr, nc = r+dr, c+dc
		if 0<=nr<n and 0<=nc<n and forest[r][c] < forest[nr][nc]:
			routes[r][c] = max(routes[r][c], dfs(nr, nc)+1)
	return routes[r][c]

if __name__ == "__main__":
	n = int(input())
	forest = [tuple(map(int, input().split())) for _ in range(n)]
	
	routes = [[0]*n for _ in range(n)]
	drc = ((-1, 0), (1, 0), (0, -1), (0, 1))

	solve()