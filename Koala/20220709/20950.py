import sys; input = sys.stdin.readline

def solve():
	
	def search(idx, k, R, G, B):
		if k > 1:
			r, g, b = target
			nr, ng, nb = R//k, G//k, B//k
			answer[0] = min(answer[0], sum(map(abs, [r-nr, g-ng, b-nb])))
		if k == 7:
			return
		for i in range(idx, n):
			r, g, b = colors[i]
			search(i+1, k+1, R+r, G+g, B+b)

	n = int(input().strip())
	colors = [[*map(int, input().split())] for _ in range(n)]
	target = [*map(int, input().split())]
	answer = [float('inf')]

	search(0, 0, 0, 0, 0)
	print(*answer)
	
solve()