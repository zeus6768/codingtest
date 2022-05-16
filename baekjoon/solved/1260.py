from collections import deque
from sys import stdin
input = stdin.readline

def solution():
	n, m, v = map(int, input().split())
	graph = [[] for _ in range(n+1)]
	for _ in range(m):
		a, b = map(int, input().split())
		graph[a].append(b)
		graph[b].append(a)
	graph = [*map(sorted, graph)]
	visited_d, visited_b = [False] * (n+1), [False] * (n+1)

	result = []
	def dfs(now):
		stack = [now]
		while stack:
			s = stack.pop()
			if not visited_d[s]:
				result.append(s)
				visited_d[s] = True
				[stack.append(i) for i in graph[s][::-1] if not visited_d[i]]
	dfs(v)
	print(*result)
	
	result = []
	def bfs(now):
		queue = deque([now])
		while queue:
			s = queue.popleft()
			if not visited_b[s]:
				result.append(s)
				visited_b[s] = True
				[queue.append(i) for i in graph[s] if not visited_b[i]]
	bfs(v)
	print(*result)

solution()