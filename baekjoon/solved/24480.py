import sys
input = sys.stdin.readline

def solve():

	def dfs(now):
		stack = [now]
		while stack:
			v = stack.pop()
			if not visited[v]:
				visited[v] = True
				answer[v-1] = count[0]
				count[0] += 1
				for i in graph[v]:
					if not visited[i]:
						stack.append(i)

	N, M, R = map(int, input().split())
	answer = [0] * N
	graph = [[] for _ in range(N+1)]
	visited = [False] * (N+1)
	count = [1]

	for _ in range(M):
		u, v = map(int, input().split())
		graph[u].append(v)
		graph[v].append(u)

	[g.sort() for g in graph]

	dfs(R)

	[print(a) for a in answer]


solve()