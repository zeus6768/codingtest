import sys, heapq
input = sys.stdin.readline

def dijkstra(n, graph, start):
	cost = [float('inf')] * (n+1)
	cost[start] = 0
	hq = [(cost[start], start)]
	while hq:
		t, x = heapq.heappop(hq)
		if cost[x] != t: continue
		for nt, nx in graph[x]:
			if cost[nx] > t + nt:
				cost[nx] = t + nt
				heapq.heappush(hq, (cost[nx], nx))
	return cost

def solve():

	for _ in range(int(input())):
		n, m = map(int, input().split())

		graph = [[]*(n+1) for _ in range(n+1)]
		for _ in range(m):
			a, b, c = map(int, input().split())
			graph[a].append((c, b))
			graph[b].append((c, a))

		answers = []
		fnum = int(input())
		frooms = [*map(int, input().split())]
		for friend in frooms:
			answers.append(dijkstra(n, graph, friend))
	
		_min = float('inf')
		for i in range(1, n+1):
			tmp = 0
			for j in range(fnum):
				tmp += answers[j][i]
			if tmp < _min:
				_min = tmp
				answer = i

		print(answer)

solve()