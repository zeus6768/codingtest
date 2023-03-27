import sys

def input():
	return sys.stdin.readline()

def solve():
	
	return

def get_distance(x1, y1, x2, y2):
	return ((x1-x2)**2 + (y1-y2)**2)**0.5

if __name__ == "__main__":
	N, W = map(int, input().split())
	M = float(input())
	stations = [tuple(map(int, input().split())) for _ in range(N)]
	graph = [[] for _ in range(N+1)]
	for _ in range(W):
		x, y = map(lambda x: int(x)-1, input().split())
		graph[x].append(y)
		graph[y].append(x)
	solve()