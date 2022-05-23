from heapq import heappop, heappush
from collections import deque
import sys
input = sys.stdin.readline

def solution():
	n, m, k, s = map(int, input().split())
	p, q = map(int, input().split())
	z_cities = [int(input()) for _ in range(k)]
	graph = [[] for _ in range(n+1)]
	for _ in range(m):
		a, b = map(int, input().split())
		graph[a].append(b)
		graph[b].append(a)

	def bfs_danger_cities(dest):
		result = [dest]
		visited = [False] * (n+1)
		visited[dest] = True
		q = deque([(dest, 0)])
		while q:
			v, depth = q.popleft()
			for i in graph[v]:
				if depth < s and not visited[i]:
					visited[i] = True
					q.append((i, depth+1))
					result.append(i)
		return result

	def dijkstra():
		cost = [float('inf')] * (n+1)
		cost[1] = 0
		hq = [(0, 1)]
		while hq:
			t, x = heappop(hq)
			if cost[x] != t or x in z_cities: continue
			for nx in graph[x]:
				if cost[nx] > t + charge[nx]:
					cost[nx] = t + charge[nx]
					heappush(hq, (cost[nx], nx))
		return cost

	charge = [p] * (n+1)
	for zc in z_cities:
		charge[zc] = float('inf')
		for city in bfs_danger_cities(zc):
			if city != zc:
				charge[city] = q
	charge[0], charge[1], charge[n] = float('inf'), 0, 0

	print(dijkstra()[n])

solution()