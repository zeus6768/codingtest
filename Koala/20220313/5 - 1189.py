def main():
	R, C, K = map(int, input().split())
	_map = [input() for _ in range(R)]
	visited = [[False]*C for _ in range(R)]
	visited[R-1][0] = True
	dd = [(-1, 0), (1, 0), (0, -1), (0, 1)]
	answer = [0]

	def go(r, c, dist):
		if (r == 0) and (c == C-1) and (dist==K):
			answer[0] += 1
			return
		for i in range(4):
			dr = r + dd[i][0]
			dc = c + dd[i][1]
			if (dr < 0) or (dr >= R) or (dc < 0) or (dc >= C) or (_map[dr][dc] == "T") or visited[dr][dc]:
				continue
			visited[dr][dc] = True
			go(dr, dc, dist+1)
			visited[dr][dc] = False
	go(R-1, 0, 1)
	print(*answer)		

main()

# correct, but not for myself