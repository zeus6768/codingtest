import sys

def input():
	return sys.stdin.readline()

def solve():
	answer = 0

	for i in range(N):
		for j in range(M):
			for tetromino in tetrominos:
				total = 0
				for dx, dy in tetromino:
					nx, ny = i+dx, j+dy
					if nx<N and ny<M:
						total += paper[nx][ny]
					else:
						break
				answer = max(answer, total)
				
	return answer

N, M = map(int, input().split())
paper = tuple(tuple(map(int, input().split())) for _ in range(N))

tetrominos = (
	((0, 0), (0, 1), (0, 2), (0, 3)),
	((0, 0), (1, 0), (2, 0), (3, 0)),

	((0, 0), (0, 1), (1, 0), (1, 1)),

	((0, 0), (1, 0), (2, 0), (2, 1)),
	((0, 0), (0, 1), (0, 2), (1, 0)),
	((0, 0), (0, 1), (1, 1), (2, 1)),
	((0, 2), (1, 0), (1, 1), (1, 2)),
	((0, 1), (1, 1), (2, 0), (2, 1)),
	((0, 0), (1, 0), (1, 1), (1, 2)),
	((0, 0), (0, 1), (1, 0), (2, 0)),
	((0, 0), (0, 1), (0, 2), (1, 2)),

	((0, 0), (1, 0), (1, 1), (2, 1)),
	((0, 1), (0, 2), (1, 0), (1, 1)),
	((0, 1), (1, 0), (1, 1), (2, 0)),
	((0, 0), (0, 1), (1, 1), (1, 2)),

	((0, 0), (0, 1), (0, 2), (1, 1)),
	((0, 1), (1, 0), (1, 1), (2, 1)),
	((0, 1), (1, 0), (1, 1), (1, 2)),
	((0, 0), (1, 0), (1, 1), (2, 0))
)

print(solve())