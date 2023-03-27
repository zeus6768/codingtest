from sys import stdin
from collections import deque

class Shark():
	
	def __init__(self, x, y):
		self.size = 2
		self.satiety = 0
		self.x = x
		self.y = y
		self.second = 0

	def move(self, x, y):
		self.x = x
		self.y = y

	def hunt(self, x, y, s=1):
		self.second += s
		self.move(x, y)
		if self.satiety+1 == self.size:
			self.size += 1
			self.satiety = 0
		else:
			self.satiety += 1

def input():
	return stdin.readline()

def solve():
	x, y, s = start
	baby_shark.hunt(x, y, s)
	ocean[x][y] = 0
	while True:
		hunt_dfs(baby_shark)
		near_fish = get_nearest_fish(baby_shark)
		if not near_fish:
			print(baby_shark.second)
			break
		x, y, s = near_fish
		baby_shark.hunt(x, y, s)
		ocean[x][y] = 0

def get_nearest_fish(shark:Shark):
	visited = [[False]*N for _ in range(N)]
	queue = deque([(shark.x, shark.y, 0)])
	candidates = list()
	while queue:
		x, y, s = queue.popleft()
		for dx, dy in dxy:
			nx, ny, ns = x+dx, y+dy, s+1
			if in_range(nx, ny) and not is_bigger_fish(nx, ny, shark.size) and not visited[nx][ny]:
				if is_edible_fish(nx, ny, shark.size):
					candidates.append((nx, ny, ns))
				queue.append((nx, ny, ns))
				visited[nx][ny] = True
	candidates.sort(key=lambda x: (x[2], x[0], x[1]))
	return candidates[0] if candidates else None

def hunt_dfs(shark:Shark):

	def _dfs(shark:Shark):
		visited[shark.x][shark.y] = True
		for dx, dy in dxy:
			nx, ny = shark.x+dx, shark.y+dy
			if is_edible_fish(nx, ny, shark.size) and not visited[nx][ny]:
				shark.hunt(nx, ny)
				ocean[nx][ny] = 0
				_dfs(shark)
				break

	visited = [[False]*N for _ in range(N)]

	_dfs(shark)

def is_bigger_fish(x, y, size):
	return ocean[x][y] > size

def is_edible_fish(x, y, size):
	return in_range(x, y) and 0 < ocean[x][y] < size

def in_range(x, y):
	return 0<=x<N and 0<=y<N

def get_shark():
	xy = [(i, j) for i in range(N) for j in range(N) if ocean[i][j]==9]
	return Shark(xy[0][0], xy[0][1])

if __name__ == "__main__":
	N = int(input())
	ocean = [list(map(int, input().split())) for _ in range(N)]

	dxy = ((-1, 0), (0, -1), (0, 1), (1, 0))

	baby_shark = get_shark()
	start = get_nearest_fish(baby_shark)
	ocean[baby_shark.x][baby_shark.y] = 0

	if start:
		solve()
	else:
		print(0)
		exit(0)


'''
5 4 0 0 3 4
4 3 0 3 4 5
3 2 0 5 6 6
2 0 0 3 4 5
3 2 0 6 5 4
6 6 6 6 6 6
'''