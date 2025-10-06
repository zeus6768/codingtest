from collections import deque
import sys

def input():
	return sys.stdin.readline().strip()

def find():
	for i in range(N):
		for j in range(M):
			if campus[i][j] == 'I':
				return (i, j)
			
def bfs(start_x, start_y):
	visited = [[False]*M for _ in range(N)]
	visited[start_x][start_y] = True
	queue = deque([(start_x, start_y)])
	count = 0
	while queue:
		x, y = queue.popleft()
		for dx, dy in dxy:
			nx, ny = x+dx, y+dy
			if in_bound(nx, ny) and not visited[nx][ny]:
				if campus[nx][ny] == 'P':
					count += 1
				visited[nx][ny] = True
				queue.append((nx, ny))
	return count if count != 0 else 'TT'
			
def in_bound(x, y):
	return 0<=x<N and 0<=y<M and campus[x][y] != 'X'

if __name__ == "__main__":

	N, M = map(int, input().split())
	campus = [input() for _ in range(N)]

	dxy = ((1, 0), (0, 1), (-1, 0), (0, -1))

	start_x, start_y = find()

	answer = bfs(start_x, start_y)

	print(answer)