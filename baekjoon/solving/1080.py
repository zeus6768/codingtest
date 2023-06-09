import sys

def input():
	return sys.stdin.readline().strip()

def turn(r, c):
	for i in range(r, r+3):
		for j in range(c, c+3):
			if diff[i][j]:
				diff[i][j] = 0
			else:
				diff[i][j] = 1
	return 1

def is_same():
	for i in range(N):
		for j in range(M):
			if diff[i][j]:
				return False
	return True

def solve():

	if is_same():
		print(0)
		return
	
	if N < 3 or M < 3:
		print(-1)
		return
	
	answer = sum([turn(i, j) for i in range(N-2) for j in range(M-2) if diff[i][j]])
	print(answer) if is_same() else print(-1)

if __name__ == "__main__":
	N, M = map(int, input().split())
	A = [list(map(int, input())) for _ in range(N)]
	B = [list(map(int, input())) for _ in range(N)]

	diff = [[int(A[i][j]!=B[i][j]) for j in range(M)] for i in range(N)]

	solve()
