# 모듈러 연산 거듭제곱
def modular_exp(x, n, m):
	y, u = 1, x % m
	while n > 0:
		if n % 2:
			y = (y*u) % m
		n //= 2
		u = (u**2) % m
	return y

# 에라토스테네스의 체
def prime(n):
	is_prime = [True] * (n+1)
	for i in range(2, int(n**0.5)+1):
		if is_prime[i]:
			for j in range(i+i, n+1, i):
				is_prime[j] = False
	return [i for i in range(2, n+1) if is_prime[i]]

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
				dfs(i)
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
from heapq import heappop, heappush
def dijkstra():

	V, E = map(int, input().split())
	K = int(input())	# 시작점
	adjacent = [[] for _ in range(V+1)]
	for _ in range(E):
		u, v, w = map(int, input().split())
		adjacent[u].append((v, w))

	def _dijkstra(s):
		cost = [float('inf')] * (V+1)
		cost[s] = 0
		hq = [[0, s]]
		while hq:
			t, x = heappop(hq)
			if cost[x] != t:
				continue
			for nx, nt in adjacent[x]:
				if cost[nx] > t + nt:
					cost[nx] = t + nt
					heappush(hq, [cost[nx], nx])
		return cost
	

