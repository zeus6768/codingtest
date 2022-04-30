import sys
input = sys.stdin.readline

def solution():
	_, Q = map(int, input().split())
	A = [*map(int, input().split())]
	for _ in range(Q):
		i, j = map(int, input().split())
		result = sum([abs(A[k] - A[k-1]) for k in range(i, j)])
		print(result)
solution()

## correct