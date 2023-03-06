from itertools import combinations as cb
from collections import deque

class Arguments:

	def __init__(self, n, edges, users, d, limit) -> None:
		self.n = n
		self.edges = edges
		self.users = users
		self.d = d
		self.limit = limit

# def bfs(graph, now, d):
# 	q = deque([(now, 0)])
# 	result = [now]
# 	while q:
# 		vp, vx = q.popleft()
# 		for np, nx in graph[vp]:
# 			if vx + nx <= d and np not in result:
# 				q.append((np, vx+nx))
# 				result.append(np)
# 	return result

def bfs2(graph, now, d):
	q = deque([(now, 0)])
	possible = [False] * len(graph)
	possible[now] = True
	while q:
		p, x = q.popleft()
		for np, nx in graph[p]:
			if x + nx <= d and not possible[np]:
				q.append((np, x+nx))
				possible[np] = True
	return possible


# 제출한 코드 (틀렸음)
# def solution(n, edges, users, d, limit):
# 	answer = 0

# 	graph = [[] for _ in range(n+1)]
# 	for p1, p2, x in edges:
# 		graph[p1].append((p2, x))
# 		graph[p2].append((p1, x))

# 	possible_visit = [bfs(graph, i+1, d) if users[i] else [] for i in range(len(users))]

# 	cases = cb(range(1, n+1), 2)

# 	for p1, p2 in cases:
# 		p1_users, p2_users = 0, 0
# 		for i in range(len(users)):
# 			if p1 in possible_visit[i]:
# 				p1_users += users[i]
# 			if p2 in possible_visit[i]:
# 				p2_users += users[i]
		
# 		p1_users = p1_users if p1_users <= limit else limit
# 		p2_users = p2_users if p2_users <= limit else limit

# 		answer = max(answer, p1_users+p2_users)
	
# 	return answer

# # 개선한 코드 (틀렸음)
# def solution1(n, edges, users, d, limit):
# 	answer = 0

# 	graph = [[] for _ in range(n+1)]
# 	for p1, p2, x in edges:
# 		graph[p1].append((p2, x))
# 		graph[p2].append((p1, x))

# 	possible_visit = [bfs(graph, i+1, d) if users[i] else [] for i in range(len(users))]

# 	cases = cb(range(1, n+1), 2)

# 	for p1, p2 in cases:
# 		p1_users, p2_users = 0, 0
# 		users_copy = users[:]
# 		for i in range(len(users)):
# 			if p1 in possible_visit[i]:
# 				if users_copy[i] < limit:
# 					p1_users += users_copy[i]
# 					users_copy[i] = 0
# 				else:
# 					p1_users += limit
# 					users_copy[i] -= limit
# 			if p2 in possible_visit[i]:
# 				if users_copy[i] < limit:
# 					p2_users += users_copy[i]
# 					users_copy[i] = 0
# 				else:
# 					p2_users += limit
# 					users_copy[i] -= limit

# 		answer = max(answer, p1_users+p2_users)
	
# 	return answer

# 최종 개선 코드
def solution3(args: Arguments):

	n, edges, users, d, limit = args.n, args.edges, args.users, args.d, args.limit
	
	answer = 0

	users = [0] + users
	
	graph = [[] for _ in range(n+1)]
	for p1, p2, x in edges:
		graph[p1].append((p2, x))
		graph[p2].append((p1, x))

	is_connected = [bfs2(graph, i, d) for i in range(n+1)]

	cases = cb(range(1, n+1), 2)

	for p1, p2 in cases:
		p1_p2_users, p1_users, p2_users = 0, 0, 0
		
		for i in range(1, n+1):
			if is_connected[p1][i] and is_connected[p2][i]:
				p1_p2_users += users[i]
			elif is_connected[p1][i]:
				p1_users += users[i]
			elif is_connected[p2][i]:
				p2_users += users[i]

		p1_users, p2_users = min(limit, p1_users), min(limit, p2_users)
		answer = max(answer, p1_users + p2_users + p1_p2_users)

	return min(answer, limit*2)


example1 = Arguments(
	7, 
	[
		[1, 2, 2], [5, 2, 2], [1, 5, 2], [1, 3, 1], 
		[1, 6, 2], [1, 7, 3], [6, 7, 4], [7, 4, 1]
	],
	[0, 2, 0, 0, 0, 4, 1], 
	2, 
	3
)

example2 = Arguments(
	6, 
	[
		[1, 2, 1], [1, 5, 1], [2, 3, 1], [2, 6, 1], [4, 5, 1]
	],
	[2, 2, 1, 1, 2, 1],
	1,
	4
)

result = solution3(example2)

print(result)