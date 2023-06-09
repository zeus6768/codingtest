def dfs(x=0, y=0, count=1):
	global answer
	answer = max(answer, count)
	for dx, dy in dxy:
		nx, ny = x + dx, y + dy
		if 0<=nx<R and 0<=ny<C and not alphabets[ord(board[nx][ny])]:
			alphabets[ord(board[nx][ny])] = 1
			dfs(nx, ny, count+1)
			alphabets[ord(board[nx][ny])] = 0

R, C = map(int, input().split())
board = [input() for _ in range(R)]

dxy = ((1, 0), (-1, 0), (0, 1), (0, -1))
alphabets = [0]*91
alphabets[ord(board[0][0])] = 1

answer = 0

dfs()

print(answer)