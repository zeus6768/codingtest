def queen(now):
	global answer
	if now == N:
		answer += 1
		return
	for i in range(N):
		board[now] = i
		for j in range(now):
			if (board[now] == board[j]) or (now-j == abs(board[now]-board[j])):
				break
		else:
			queen(now+1)
	return

if __name__ == "__main__":
	N = int(input())
	board = [0]*N
	answer = 0

	queen(0)
	print(answer)