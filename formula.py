# 최대공약수 GCD
def gcd(x, y):
	while y:
		x, y = y, x % y
	return x

# 최소공배수 LCM
def lcm(x, y):
	return x * y // gcd(x, y)

# DFS - 스택
def dfs_stack():
	graph, visited, result = [], [], []
	def dfs(now):
		stack = [now]
		while stack:
			v = stack.pop()
			if not visited[v]:
				result.append(v)
				visited[v] = True
				for i in graph[v]:
					if not visited[i]:
						stack.append(i)
	return result

# DFS - 재귀
def dfs_recursive():
	graph, visited, result = [], [], []
	def dfs(now):
		visited[now] = True
		result.append(now)
		for i in graph[now]:
			if not visited[i]:
				dfs_recursive(i)
	return result

# BFS - 큐
from collections import deque
def bfs():
	graph, visited, result = [], [], []
	def _bfs(now):
		q = deque([now])
		visited[now] = True
		result.append(now)
		while q:
			v = q.popleft()
			for i in graph[v]:
				if not visited[i]:
					q.append(i)
					visited[i] = True
					result.append(i)
	return result

# 다익스트라 Dijkstra
from heapq import *
n = int(input())
adj = [[] for _ in range(n+1)]
def dijkstra(s):
	cost = [float('inf')] * (n+1)
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