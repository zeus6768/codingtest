from sys import stdin

def input():
	return stdin.readline()

def main():

	N, M, R = map(int, input().split())
	A = [list(map(int, input().split())) for _ in range(N)]
	
	K = min(N, M) // 2

	for _ in range(R):
		answer = [[0]*M for _ in range(N)]
		for k in range(K):
			for j in range(N-1-k*2):
				answer[k+j+1][k] = A[k+j][k]
				answer[k+j][M-k-1] = A[k+j+1][M-k-1]
			for j in range(M-1-k*2):
				answer[k][k+j] = A[k][k+j+1]
				answer[N-k-1][k+j+1] = A[N-k-1][k+j]
		A = answer

	[print(*a) for a in answer]

main()
