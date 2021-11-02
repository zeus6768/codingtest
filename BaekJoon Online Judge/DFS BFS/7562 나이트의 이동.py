n = int(input())

def bfs(visited: list, start: tuple, end: tuple) -> int:
	to_visit, count = [start], 0
	d = (	
		(-2, 1), (-1, 2), (1, 2), (2, 1),
		(2, -1), (1, -2), (-1, -2), (-2, -1)
	)
	
	while to_visit:
		node = to_visit.pop(0)
		print(node)
		if node == end:
			return count
		elif not visited[node[0]][node[1]]:
			visited[node[0]][node[1]] = True
			for i in range(8):
				x, y = node[0]+d[i][0], node[1]+d[i][1]
				if (0 <= x < len(visited)) and (0 <= y < len(visited)):
					to_visit.append((x, y))
			count += 1



for i in range(n):
	l = int(input())
	field = [[False]*l for _ in range(l)]
	as_is = tuple(map(int, input().split()))
	to_go = tuple(map(int, input().split()))

	result = bfs(field, as_is, to_go)
	print(result)