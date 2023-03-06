from collections import deque
import sys
input = sys.stdin.readline

def solve():

	def bfs(R):
		
		return

	N, M, R = map(int, input().split())

	graph = [[] for _ in range(N+1)]

	for _ in range(M):
		u, v = map(int, input().split())
		graph[u].append(v)
		graph[v].append(u)

	visited = [False] * (N+1)

	return