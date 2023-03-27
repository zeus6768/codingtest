from collections import deque

def input():
	return __import__('sys').stdin.readline()

def main():
	answer = 0
	for i in range(1, N+1):
		if not visited[i]:
			bfs(i)
			answer += 1
	print(answer)
	return

def bfs(now):
	visited[now] = True
	queue = deque([now])
	while queue:
		node = queue.popleft()
		for i in graph[node]:
			if not visited[i]:
				queue.append(i)
				visited[i] = True
	return

if __name__ == "__main__":
	N, M = map(int, input().split())
	graph = [list() for _ in range(N+1)]
	for _ in range(M):
		u, v = map(int, input().split())
		graph[u].append(v)
		graph[v].append(u)
	visited = [False] * (N+1)
	main()