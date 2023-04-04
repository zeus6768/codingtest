def input():
	return __import__('sys').stdin.readline()

def solve():
	for i in range(N):
		w, v = items[i]
		for j in range(K+1):
			if j < w:
				bag[i][j] = bag[i-1][j]
			else:
				bag[i][j] = max(bag[i-1][j], bag[i-1][j-w]+v)
	[print(b) for b in bag]
	print(bag[-1])

def solve2():
	for item in items:
		w, v = item
		for i in range(w, K+1):
			bag2[i] = max(bag2[i], bag2[i-w]+v)
	print(bag2)
	print(bag2[-1])

if __name__ == "__main__":
	N, K = map(int, input().split())
	items = [tuple(map(int, input().split())) for _ in range(N)]
	bag = [[0] * (K+1) for _ in range(N)]
	bag2 = [0] * (K+1)
	solve()
	print()
	solve2()