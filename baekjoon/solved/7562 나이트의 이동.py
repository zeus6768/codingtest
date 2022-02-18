import math

n = int(input())

def bfs(visited: list, start: tuple, end: tuple) -> int:
	to_visit, count = [start], 0
	d = (	
		(-2, 1), (-1, 2), (1, 2), (2, 1),
		(2, -1), (1, -2), (-1, -2), (-2, -1)
	)
	
	while to_visit:
		node = to_visit.pop(0)
		if node == end:
			print(count)
			return int(math.log(count, 8))
		elif not visited[node[0]][node[1]]:
			visited[node[0]][node[1]] = True
			for i in range(8):
				x, y = node[0]+d[i][0], node[1]+d[i][1]
				if (0 <= x < len(visited)) and (0 <= y < len(visited)) and ():
					to_visit.append((x, y))
			count += 1

for i in range(n):
	l = int(input())
	depth = [[0]*l for _ in range(l)]
	as_is = tuple(map(int, input().split()))
	to_go = tuple(map(int, input().split()))

	result = bfs(depth, as_is, to_go)
	print(result)