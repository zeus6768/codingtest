from collections import deque
import sys

def input():
	return sys.stdin.readline()

def bfs(node):
	visited = [False] * N
	queue = deque()
	queue.append(node)
	while queue:
		now = queue.popleft()
		for i in range(N):
			route_exists = G[now][i]
			if route_exists and not visited[i]:
				queue.append(i)
				visited[i] = True
				answer[node][i] = 1

N = int(input())
G = [tuple(map(int, input().split())) for _ in range(N)]

answer = [[0]*N for _ in range(N)]

[bfs(node) for node in range(N)]

[print(*a) for a in answer]