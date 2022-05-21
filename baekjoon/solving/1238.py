from heapq import *
import sys
input = sys.stdin.readline
INF = sys.maxsize

def solution():

	def dijkstra(s):
		cost = [INF] * (n+1)
		cost[s] = 0
		hq = [[0, s]]
		while hq:
			t, x = heappop(hq)
			if cost[x] != t:
				continue
			for nx, nt in adj[x]:
				if cost[nx] > t + nt:
					cost[nx] = t + nt
					heappush(hq, [cost[nx], nx])
		return cost

	n, m, x = map(int, input().split())
	adj = [[] for _ in range(n+1)]
	for i in range(m):
		s, e, t = map(int, input().split())
		adj[s].append([e, t])

	timeStart = [0] * (n+1)
	for i in range(1, n+1):
		time = dijkstra(i)
		timeStart[i] = time[x]
	timeEnd = dijkstra(x)

	print(max(timeStart[i] + timeEnd[i] for i in range(1, n+1)))
	
solution()