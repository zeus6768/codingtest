from heapq import *
input = __import__('sys').stdin.readline

def solution():
	def dijkstra(n, graph):
		drc = ((-1, 0), (1, 0), (0, -1), (0, 1))
		cost = [[float('inf')] * n for _ in range(n)]
		cost[0][0] = graph[0][0]
		hq = [(graph[0][0], 0, 0)]
		while hq:
			t, r, c = heappop(hq)
			if cost[r][c] != t: continue
			for dr, dc in drc:
				nr, nc = r + dr, c + dc
				if (0 <= nr < n) and (0 <= nc < n) and (cost[nr][nc] > t + graph[nr][nc]):
					cost[nr][nc] = t + graph[nr][nc]
					heappush(hq, (cost[nr][nc], nr, nc))
		return cost[n-1][n-1]

	num = 1
	while True:
		n = int(input())
		if n == 0: return
		graph = [[*map(int, input().split())] for _ in range(n)]
		answer = dijkstra(n, graph)
		print(f"Problem {num}: {answer}")
		num += 1

solution()