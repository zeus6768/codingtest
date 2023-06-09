from heapq import heappop, heappush

def dijkstra(node):
	costs = [float("inf")] * 100_001
	costs[node] = 0
	hq = [(0, node)]
	while hq:
		cost, now = heappop(hq)
		if cost != costs[now]:
			continue
		if now != 0 and (cost+1 < costs[now-1]):
			costs[now-1] = cost+1
			heappush(hq, (costs[now-1], now-1))
		if now != 100_000 and (cost+1 < costs[now+1]):
			costs[now+1] = cost+1
			heappush(hq, (costs[now+1], now+1))
		if now <= 50_000 and cost < costs[now*2]:
			costs[now*2] = cost
			heappush(hq, (costs[now*2], now*2))
	return costs[K]

N, K = map(int, input().split())
print(dijkstra(N))