import sys
input = sys.stdin.readline

def solve():

	def bfs(w, h):
		count = 0
		queue = []

		for i in range(h):
			for j in range(w):
				if visited[i][j] == False and _map[i][j] == 1:
					
					queue.append([i, j])
					visited[i][j] = True

					while True:
						r, c = queue.pop()
						for k in range(8):
							nr = r + drc[k][0]
							nc = c + drc[k][1]
							if 0 <= nr < h and 0 <= nc < w:
								if visited[nr][nc] == False and _map[nr][nc] == 1:
									visited[nr][nc] = True
									queue.append([nr, nc])
						if not queue:
							count += 1
							break
		print(count)

	drc = ((1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1))

	while True:
		w, h = map(int, input().split())
		if w == h == 0: break
		_map = [[*map(int, input().split())] for _ in range(h)]
		visited = [[False] * w for _ in range(h)]
		bfs(w, h)
	
solve()