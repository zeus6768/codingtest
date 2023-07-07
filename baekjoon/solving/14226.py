from collections import deque

def bfs():
	q = deque([(1, 0, 0)])
	while q:
		now, clipboard, time = q.popleft()
		if now == S:
			return time
		for op in range(3):
			new, new_clipboard = now, clipboard
			if op == 0:
				new_clipboard = now
			elif op == 1 and clipboard and new + clipboard <= S+1:
				new += clipboard
			elif op == 2 and now > 2:
				new -= 1
			else:
				continue
			if not visited[new][new_clipboard]:
				visited[new][new_clipboard] = True
				q.append((new, new_clipboard, time+1))

S = int(input())
visited = [[False]*(1002) for _ in range(1002)]
print(bfs())