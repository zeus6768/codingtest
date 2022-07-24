import sys; input = sys.stdin.readline

def solve():
	n, m = map(int, input().split())
	pocket1 = {input().strip():i for i in range(1, n+1)}
	pocket2 = {pocket1[i]:i for i in pocket1}

	for _ in range(m):
		s = input().strip()
		if s.isdecimal():
			print(pocket2[int(s)])
		else:
			print(pocket1[s])

solve()
