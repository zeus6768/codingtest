from heapq import heappop, heappush
from sys import stdin
input = stdin.readline

def dijkstra(n, start, graph):
	distance = [float('inf')] * (n+1)
	distance[start] = 0
	dp = [0 for _ in range(n+1)]
	dp[start] = 1
	hq = [(0, start)]
	while hq:
		t, x = heappop(hq)
		if distance[x] < t: continue
		for nx, nt in graph[x]:
			# print(f">> 출발지 {start} 에서 노드 {x} 까지의 거리는 {t}입니다. {x}에서 {nx}까지의 거리는 {nt}입니다. ")
			if t + nt < distance[nx]:
				# print(f">>\t distance[{nx}]를 업데이트합니다. {distance[nx]} -> {t+nt}\n")
				distance[nx] = t + nt
				heappush(hq, (distance[nx], nx))
			if distance[nx] < t:
				dp[x] += dp[nx]
				# print(f">>\t{distance[nx]} < {t}이므로{x} -> {nx}는 {start}로 향하는 합리적인 이동경로입니다. 노드 {x}의 합리적인 이동경로 개수는 {dp[x]}개 입니다. \n")
	return dp

def main():
	N, M = map(int, input().split())
	graph = [[] for _ in range(N+1)]
	for _ in range(M):
		A, B, C = map(int, input().split())
		graph[A].append((B, C))
		graph[B].append((A, C))
	cost = dijkstra(N, 2, graph)
	print(cost[1])

main()