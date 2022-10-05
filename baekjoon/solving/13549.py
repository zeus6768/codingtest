import sys, heapq
input = sys.stdin.readline

def Dijkstra(n, graph, start):
	cost = [float('inf')] * (n+1)
	cost[start] = 0
	heap = [(cost[start], start)]
	while heap:
		t, now = heapq.heappop(heap)
		if cost[now] < t:
			continue
		for w, next_node in graph[now]:
			nt = w + t
			if nt < cost[next_node]:
				cost[next_node] = nt
				heapq.heappush(heap, (nt, next_node))
	return cost
	

def solve():
	V, E = map(int, input().split())
	K = int(input())
	graph = [[] for _ in range(V + 1)]

	for _ in range(E):
		u, v, w = map(int, input().split())
		graph[u].append((w, v))
	
	cost = Dijkstra(V, graph, K)

	[print(cost[i] if cost[i] != float('inf') else "INF") for i in range(1, V+1)]


solve()