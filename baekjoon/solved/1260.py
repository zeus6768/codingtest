from collections import deque
from sys import stdin
input = stdin.readline

def main():
	n, m, v = map(int, input().split())
	nodes = [[]]
	[nodes.append([]) for _ in range(n)]
	for _ in range(m):
		s, d = map(int, input().split())
		nodes[s].append(d)
		nodes[d].append(s)
	nodes = [sorted(nodes[i]) for i in range(n+1)]
	d_visited = [False] * (n+1)
	b_visited = [False] * (n+1)
	
	d_route = []
	b_route = []

	def dfs(now):
		d_route.append(now)
		d_visited[now] = True
		[dfs(i) for i in nodes[now] if not d_visited[i]]

	def bfs(now):
		b_visited[now] = True
		queue = deque([now])
		b_route.append(now)
		while queue:
			v = queue.popleft()
			for i in nodes[v]:
				if not b_visited[i]:
					queue.append(i)
					b_visited[i] = True
					b_route.append(i)

	dfs(v)
	print(*d_route)
	bfs(v)
	print(*b_route)

main()
