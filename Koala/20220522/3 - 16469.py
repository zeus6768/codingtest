from collections import deque
import sys
input = sys.stdin.readline

def solution():
	r, c = map(int, input().split())
	maze = [input().strip() for _ in range(r)]
	villian = [[*map(lambda x: int(x)-1, input().split())] for _ in range(3)]

	drc = ((-1, 0), (1, 0), (0, -1), (0, 1))
	def bfs(cx, cy):
		cost = [[float('inf') for _ in range(c)] for _ in range(r)]
		cost[cx][cy] = 0
		que = deque([(cx, cy)])
		while que:
			x, y = que.popleft()
			for dx, dy in drc:
				nx, ny = x + dx, y + dy
				if (0 <= nx < r) and (0 <= ny < c) and cost[nx][ny] == float('inf') and maze[nx][ny] == '0':
					que.append((nx, ny))
					cost[nx][ny] = cost[x][y] + 1
		return cost

	vr1 = bfs(villian[0][0], villian[0][1])
	vr2 = bfs(villian[1][0], villian[1][1])
	vr3 = bfs(villian[2][0], villian[2][1])
	dist, answer = float('inf'), 0

	for i in range(r):
		for j in range(c):
			d = max(vr1[i][j], vr2[i][j], vr3[i][j])
			if dist > d :
				answer = 1
				dist = d
			elif dist == d :
				answer += 1
	print(f"{dist}\n{answer}" if dist < float('inf') else -1)

solution()