from collections import deque
import sys

def input():
	return sys.stdin.readline().strip()

def find_goal():
	for i in range(n):
		for j in range(m):
			if MAP[i][j] == 2:
				return (i, j)

def bfs(start_x, start_y):
	visited = [[False]*m for _ in range(n)]
	visited[start_x][start_y] = True
	queue = deque([(start_x, start_y, 0)])
	while queue:
		x, y, d = queue.popleft()
		for dx, dy in dxy:
			nx, ny = x+dx, y+dy
			if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and MAP[nx][ny] != 0:
				answer[nx][ny] = d+1
				queue.append((nx, ny, d+1))
				visited[nx][ny] = True

if __name__ == "__main__":
	n, m = map(int, input().split())
	MAP = [tuple(map(int, input().split())) for _ in range(n)]
	
	goal_x, goal_y = find_goal()
	dxy = ((1, 0), (-1, 0), (0, 1), (0, -1))

	answer = [[-1 if MAP[i][j]!=0 else 0 for j in range(m)] for i in range(n)]
	answer[goal_x][goal_y] = 0

	bfs(goal_x, goal_y)
	
	[print(*a) for a in answer]