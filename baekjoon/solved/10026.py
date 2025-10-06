from collections import deque
import sys

def input():
	return sys.stdin.readline().strip()

def solve():
	answer_normal, answer_weak = 0, 0
	for i in range(N):
		for j in range(N):
			if not visited_normal[i][j]:
				normal(i, j, drawing[i][j])
				answer_normal += 1
			if not visited_weak[i][j]:
				color_weak(i, j, drawing[i][j])
				answer_weak += 1
	print(answer_normal, answer_weak)

def normal(x_init, y_init, color):
	visited_normal[x_init][y_init] = True
	queue = deque([(x_init, y_init)])
	while queue:
		x, y = queue.popleft()
		for dx, dy in dxy:
			nx, ny = x+dx, y+dy
			if in_bound(nx, ny) and drawing[nx][ny] == color and not visited_normal[nx][ny]:
				queue.append((nx, ny))
				visited_normal[nx][ny] = True

def color_weak(x_init, y_init, color):
	visited_weak[x_init][y_init] = True
	queue = deque([(x_init, y_init)])
	while queue:
		x, y = queue.popleft()
		for dx, dy in dxy:
			nx, ny = x+dx, y+dy
			if in_bound(nx, ny) and not visited_weak[nx][ny]:
				if possible(nx, ny, color):
					queue.append((nx, ny))
					visited_weak[nx][ny] = True

def in_bound(x, y):
	return 0<=x<N and 0<=y<N

def possible(x, y, color):
	if color in weak_colors:
		return drawing[x][y] in weak_colors
	return drawing[x][y] == color


N = int(input())
drawing = tuple(input() for _ in range(N))

weak_colors = "RG"

dxy = ( (-1, 0), (1, 0), (0, -1), (0, 1) )

visited_normal = [[False]*N for _ in range(N)]
visited_weak = [[False]*N for _ in range(N)]

solve()
