input = __import__("sys").stdin.readline

def solve(arr):
	chessboard = ['WB'*4 if i%2 else 'BW'*4 for i in range(8)]
	cnt1, cnt2 = 0, 0
	for i in range(8):
		for j in range(8):
			if arr[i][j] != chessboard[i][j]:
				cnt1 += 1
			else:
				cnt2 += 1
	return min(cnt1, cnt2)

def main():
	n, m = map(int, input().split())
	board = [input().strip() for _ in range(n)]
	answer = float('inf')
	for i in range(n-7):
		for j in range(m-7):
			tmp = []
			for k in range(8):
				tmp.append(board[i+k][j:j+8])
			r = solve(tmp)
			answer = min(answer, r)
	print(answer)

main()
