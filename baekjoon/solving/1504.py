from heapq import *
input = __import__('sys').stdin.readline
miis = lambda: map(int, input().split())

def solution():
	n, e = miis()
	adj = [[] for _ in range(n+1)]
	for _ in range(e):
		a, b, c = miis()
		adj[a].append([b, c])
		adj[b].append([a, c])
	v1, v2 = miis()

	def dijkstra(s):
		cost = [float('inf')] * (n+1)
		cost[s] = 0
		hq = [(0, s)]
		while hq:
			t, x = heappop(hq)
			if cost[x] != t: continue
			for nx, nt in adj[x]:
				if cost[nx] > t + nt:
					cost[nx] = t + nt
					heappush(hq, (cost[nx], nx))
		return cost

	d1, dv1, dv2 = dijkstra(1), dijkstra(v1), dijkstra(v2)
	result = min(d1[v1]+dv1[v2]+dv2[n],	d1[v2]+dv2[v1]+dv1[n])
	print(result) if result != float('inf') else print(-1)

solution()