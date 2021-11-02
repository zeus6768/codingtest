import sys
input = sys.stdin.readline

graph = {}
n, m, v = map(int, input().split())
for _ in range(m):
	node1, node2 = map(int, input().split())
	if node1 in graph:
		graph[node1].append(node2)
	else:
		graph[node1] = [node2]

	node1, node2 = node2, node1
	if node1 in graph:
		graph[node1].append(node2)
	else:
		graph[node1] = [node2]

[graph[i].sort() for i in graph]

def dfs(graph, start):
	to_visit, visited = [start], []
	while to_visit:
		node = to_visit.pop()
		if node not in visited:
			visited.append(node)
			to_visit.extend(graph[node][::1])
	return visited

def bfs(graph, start):
	to_visit, visited = [start], []
	while to_visit:
		node = to_visit.pop(0)
		if node not in visited:
			visited.append(node)
			to_visit.extend(graph[node])
	return visited

print(dfs(graph, v))
print(bfs(graph, v))