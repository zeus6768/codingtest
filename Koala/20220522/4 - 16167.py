import sys
from heapq import *
input = sys.stdin.readline

def solution():
	n, r = map(int, input().split())
	info = [[*map(int, input().split())] for _ in range(r)]
	graph = [[] for _ in range(n+1)]
	for src, des, fc, ac, ti in info:
		cost = fc + (ti-10)*ac if ti > 10 else fc
		graph[src].append((des, cost))
	
	def dijkstra():
		cost = [[float('inf')]*2 for _ in range(n+1)]
		cost[1] = [0, 1]
		hq = [(0, 1, 1)]
		while hq:
			t, d, x = heappop(hq)
			if cost[x][0] != t: continue
			for nx, nt in graph[x]:
				if cost[nx][0] > t + nt or (cost[nx][0] == t + nt and cost[nx][1] > d + 1):
					cost[nx][0] = t + nt
					cost[nx][1] = d + 1
					heappush(hq, (cost[nx][0], cost[nx][1], nx))
		return cost

	answer = dijkstra()

	print(*answer[n]) if answer[n][0] != float('inf') else print("It is not a great way.")

solution()