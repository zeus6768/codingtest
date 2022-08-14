import sys
input = sys.stdin.readline

def solve():
	n, q = map(int, input().split())
	A = [*map(int, input().split())]

	psum = [0]
	[psum.append(psum[i] ^ A[i]) for i in range(n)]

	answer = 0

	for _ in range(q):
		s, e = map(int, input().split())
		tmp = psum[e] ^ psum[s-1]
		answer = answer ^ tmp
	
	print(answer)


solve()