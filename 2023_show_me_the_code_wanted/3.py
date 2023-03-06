miis = lambda: map(int, input().split())

N, M, C = miis()
W = [list(miis()) for _ in range(C)]
A = list(miis())
B = list(miis())

answer = 0

if N < M:
	A, B = B, A
	N, M = M, N


for i in range(N+M-1):
	total = 0
	for j in range(M):
		if 0 <= (i-M+1) < N:
			a, b = A[i-M+1]-1, B[j]-1
			total += W[a][b]
	answer = max(answer, total)

print(answer)

'''
(0, M-1)
(0, M-2), (1, M-1)
(0, M-3), (1, M-2), (2, M-1)
(0, M-4), (1, M-3), (2, M-2), (3, M-1)
(0, M-5), (1, M-4), (2, M-3), (3, M-2), (4, M-1)
...
N, M = 4, 3
A = [1, 2, 3, 4]
B = [3, 4, 5]
1) {A[-2], B[0]}, {A[-1], B[1]}, (A[0], B[2])
2) {A[-1], B[0]}, (A[0], B[1]), (A[1], B[2])
3) (A[0], B[0]), (A[1], B[1]), (A[2], B[2])
4) (A[1], B[0]), (A[2], B[1]), (A[3], B[2])
5) (A[2], B[0]), (A[3], B[1]), {A[4], B[2]}
6) (A[3], B[0]), {A[4], B[1]}, {A[5], B[2]}

for i in range(N+M-1):
	for j in range(M):
		if 0 <= (i-M+1) < N:
			a, b = A[i-M+1], B[j]
		

'''