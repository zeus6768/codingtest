from heapq import heappop, heappush
import sys

def input():
	return sys.stdin.readline()

def solve():
	d = dijkstra()
	print(int(d[-1]*1000))

def dijkstra(start=0):
	cost = [float('inf')] * N
	cost[start] = 0
	hq = [(0, start)]
	while hq:
		t, v = heappop(hq)
		if cost[v] != t:
			continue
		for nv, nt in enumerate(distances[v]):
			if t + nt < cost[nv]:
				cost[nv] = t + nt
				heappush(hq, (cost[nv], nv))
	return cost

def get_distance(p1, p2):
	return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

if __name__ == "__main__":
	N, W = map(int, input().split())
	M = float(input())
	stations = [tuple(map(int, input().split())) for _ in range(N)]
	distances = [[get_distance(stations[i], stations[j]) for i in range(N)] for j in range(N)]
	for _ in range(W):
		s1, s2 = map(lambda x: int(x)-1, input().split())
		distances[s1][s2] = 0
		distances[s2][s1] = 0
	solve()