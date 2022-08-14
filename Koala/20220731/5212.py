import sys
input = sys.stdin.readline

def solve():
	r, c = map(int, input().split())
	_map = [input().strip() for _ in range(r)]

	drc = [(-1, 0), (0, 1), (1, 0), (0, -1)]

	n_map = [['.']*c for _ in range(r)]

	min_r, max_r, min_c, max_c = r, 0, c, 0

	for i in range(r):
		for j in range(c):
			if _map[i][j] == 'X':
				sea_count = 0
				for k in range(4):
					nr, nc = i + drc[k][0], j + drc[k][1]
					if nr < 0 or nc < 0 or nr >= r or nc >= c or _map[nr][nc] == '.':
						sea_count += 1
				if sea_count < 3:
					min_r, max_r = min(min_r, i), max(max_r, i)
					min_c, max_c = min(min_c, j), max(max_c, j)
					n_map[i][j] = 'X'


	answer = [n_map[min_r+i][min_c:max_c+1] for i in range(max_r - min_r + 1)]

	[print("".join(a)) for a in answer]


solve()