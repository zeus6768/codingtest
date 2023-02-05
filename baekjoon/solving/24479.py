import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solve():

	def dfs(R):
		visited[R] = True
		answer[R-1] = count[0]
		count[0] += 1
		for x in graph[R]:
			if not visited[x]:
				dfs(x)

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