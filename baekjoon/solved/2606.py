from collections import deque
import sys
input = sys.stdin.readline

def bfs(n, graph):
	visited = [False] * (n+1)
	visited[1] = True
	queue = deque([1])
	while queue:
		now = queue.popleft()
		for next in graph[now]:
			if not visited[next]:
				visited[next] = True
				queue.append(next)
	return visited

def solve():

	N = int(input())

	graph = [[] for _ in range(N+1)]
	for _ in range(int(input())):
		a, b = map(int, input().split())
		graph[a].append(b)
		graph[b].append(a)

	result = bfs(N, graph)
	print(sum(result)-1)
	
solve()