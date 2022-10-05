from collections import deque
import sys
input = sys.stdin.readline

def distance(r1, c1, r2, c2):
	return abs(r1-r2) + abs(c1-c2)

def solve():
	n, m, k = map(int, input().split())
	
	store, column, chair = [], [], []

	for i in range(n):
		tmp = [*map(int, input().split())]
		store.append(tmp)
		if 4 in tmp: siru = (i, tmp.index(4), 1)
		if 3 in tmp: column.append((i, tmp.index(3)))
		if 2 in tmp: chair.append((i, tmp.index(2)))
	
	drc = ((1, 0), (0, 1), (-1, 0), (0, -1))

	for r, c in column:
		q = deque([(r, c)])
		while q:
			x, y = q.popleft()
			for dr, dc in drc:
				nr, nc = x + dr, y + dc
				d = distance(nr, nc, r, c)
				if 0 <= nr < n and 0 <= nc < m and d <= k and store[nr][nc] in [0, 2]:
					store[nr][nc] = 1
					q.append((nr, nc))

	q = deque([siru])
	visited = [[False]*m for _ in range(n)]
	visited[siru[0]][siru[1]] = True
	while q:
		x, y, z = q.popleft()
		for dr, dc in drc:
			nr, nc = x + dr, y + dc
			if 0 <= nr < n and 0 <= nc < m and store[nr][nc] == 2:
				print(z)
				return
			elif 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and store[nr][nc] == 0:
				q.append((nr, nc, z+1))
				visited[nr][nc] = True

	print(-1)


solve()

# 3%에서 틀림