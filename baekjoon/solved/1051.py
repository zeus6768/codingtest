input = __import__('sys').stdin.readline

def solve():
	n, m = map(int, input().split())
	square = [input().strip() for _ in range(n)]
	extent = 1
	for i in range(n-1):
		for j in range(m-1):
			for k in range(1, min(n, m)):
				tmp = (k+1)**2
				if (
					extent < tmp and 
					i+k < n and j+k < m and
					square[i][j] == square[i+k][j] == square[i][j+k] == square[i+k][j+k]
				):
					extent = tmp
	print(extent)
solve()