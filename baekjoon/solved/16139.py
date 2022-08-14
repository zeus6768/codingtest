import sys
input = sys.stdin.readline

def solve():
	S = input().strip()
	size = len(S)
	q = int(input())
	psum = {}

	for _ in range(q):
		a, l, r = input().split()
		l, r = int(l), int(r)
		if a not in psum:
			psum[a] = [0]
			[psum[a].append(psum[a][i-1] + (a==S[i-1])) for i in range(1, size+1)]
		print(psum[a][r+1] - psum[a][l])

solve()