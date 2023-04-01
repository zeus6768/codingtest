from sys import stdin

def input():
	return stdin.readline().strip()

def one_second():
	installed, bombed = list(), list()
	for i in range(R):
		for j in range(C):
			if timer[i][j] in (-1, 0, 1):
				installed.append((i, j))
			if timer[i][j] == 2:
				bombed.append((i, j))
				bombed.extend(bomb(i, j))
	for x, y in installed:
		timer[x][y] += 1
	for x, y in bombed:
		timer[x][y] = -1

def bomb(r, c):
	return [(r+x, c+y) for x, y in dxy if 0<=r+x<R and 0<=c+y<C]
			
def print_graph():
	gr = [[EMPTY if timer[i][j]==0 else BOMB for j in range(C)]for i in range(R)]
	[print(''.join(g)) for g in gr]

if __name__ == "__main__":
	R, C, N = map(int, input().split())
	graph = [list(input()) for _ in range(R)]
	
	EMPTY, BOMB = '.', 'O'
	dxy = ((1, 0), (-1, 0), (0, 1), (0, -1))

	timer = [[2 if graph[i][j]==BOMB else 0 for j in range(C)] for i in range(R)]

	[one_second() for _ in range(N-1)]
	print_graph()