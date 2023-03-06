import sys
sys.setrecursionlimit(1000000)

def main():

	def queen(now):
		if now == N:
			answer[0] += 1
			return
		for i in range(N):
			board.append(i)
			if possible(now):
				queen(now+1)
			board.pop()
		return
	
	def possible(k):
		for i in range(k):
			if (board[i] == board[k]) or (abs(i-k) == abs(board[i]-board[k])):
				return False
		return True

	N = int(input())
	answer = [0]
	board = []
	queen(0)
	print(*answer)

main()