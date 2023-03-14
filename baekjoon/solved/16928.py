from collections import deque

def input():
	return __import__('sys').stdin.readline()

def main():
	answer = bfs(1)
	print(answer)

def bfs(start):
	visited = [False] * 101
	queue = deque([(start, 0)])
	while queue:
		now, count = queue.popleft()
		if now == END:
			return count
		for i in range(1, 7):
			new = now + i
			if new <= END and not visited[new]:
				visited[new] = True
				while new in ladders:
					new = ladders[new]
					visited[new] = True
				queue.append((new, count+1))

N, M = map(int, input().split())
ladders = dict()
for _ in range(N+M):
	x, y = map(int, input().split())
	ladders[x] = y

END = 100

main()