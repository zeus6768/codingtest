import sys
input = sys.stdin.readline

def solve():
	n, q = map(int, input().split())
	A = sorted(map(int, input().split()))

	csum = [0]*(n+1)
	for i in range(n):
		csum[i+1] = csum[i] + A[i]
	
	for _ in range(q):
		l, r = map(int, input().split())
		print(csum[r]-csum[l-1])

solve()

# 2 5 1 4 3 => 1 2 3 4 5
# 1 5 => 1 + 2 + 3 + 4 + 5 = 15
