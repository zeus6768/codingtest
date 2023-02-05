from sys import stdin
from heapq import heappop, heappush

input = stdin.readline

def solve():

	def dijkstra(start):
		
		cost = [float('inf')] * (N+1)
		cost[start] = 0
		hq = [(0, start)]

		while hq:
			t, x = heappop(hq)
			if t != cost[x]:
				continue
			for nx, nt in graph[x]:
				if t + nt < cost[nx]:
					cost[nx] = t + nt
					heappush(hq, (cost[nx], nx))
		
		return cost

	N, M, X = map(int, input().split())
	
	graph = [[] for _ in range(N+1)]
	for _ in range(M):
		S, D, T = map(int, input().split())
		graph[S].append((D, T))

	answer = 0
	way_home = dijkstra(X)

	for i in range(1, N+1):
		way_party = dijkstra(i)
		answer = max(answer, way_party[X] + way_home[i])

	print(answer)


solve()