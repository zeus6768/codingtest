def solve():
	R, C, K = map(int, input().split())
	graph = [input() for _ in range(R)]
	visited = [[False]*C for _ in range(R)]
	drc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
	answer = [0]

	def go(r, c, distance):
		if r == 0 and c == C-1 and distance == K:
			answer[0] += 1
			return
		else:
			for i in range(4):
				dr = r + drc[i][0]
				dc = c + drc[i][1]
				if 0<=dr<R and 0<=dc<C and graph[dr][dc]!='T' and not visited[dr][dc]:
					visited[dr][dc] = True
					go(dr, dc, distance+1)
					visited[dr][dc] = False

	go(R-1, 0, 1)
	print(*answer)

solve()