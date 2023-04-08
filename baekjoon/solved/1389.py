from heapq import heappop, heappush
import sys

def input():
	return sys.stdin.readline()

def solve():
	for i in range(N):
		dijkstra(i)
	answer = -1
	_min = float('inf')
	for i in range(N):
		t = sum(kevin_bacon[i])
		if t < _min:
			_min = t
			answer = i
	print(answer+1)

def dijkstra(start):
	cost = [float('inf')] * (N)
	cost[start] = 0
	hq = [(0, start)]
	while hq:
		c, now = heappop(hq)
		if cost[now] != c:
			continue
		for n in relations[now]:
			if c+1 < cost[n]:
				cost[n] = c+1
				heappush(hq, (c+1, n))
	kevin_bacon.append(cost)

if __name__ == "__main__":
	N, M = map(int, input().split())
	relations = [set() for _ in range(N)]
	for _ in range(M):
		a, b = map(lambda x:int(x)-1, input().split())
		relations[a].add(b)
		relations[b].add(a)

	kevin_bacon = list()

	solve()

"""
5 5
2 1
1 2
1 4
3 4
4 5

"""