import sys
input = sys.stdin.readline

def solve():
	n, q = map(int, input().split())
	domino = [*map(int, input().split())]
	for _ in range(q):
		t, *xyd = map(int, input().split())

		if t == 0:
			x, y = xyd
			answer = domino[x] ^ domino[y]
			...
		else:
			x, y, d = xyd
			
			...

		print(answer)