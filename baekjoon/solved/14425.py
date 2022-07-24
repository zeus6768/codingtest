import sys; input = sys.stdin.readline

def solve():
	n, m = map(int, input().split())
	S = {input().strip() for _ in range(n)}
	print(sum([input().strip() in S for _ in range(m)]))
	
solve()