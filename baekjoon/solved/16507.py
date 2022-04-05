import sys
input = sys.stdin.readline

def main():
	r, c, q = map(int, input().split())
	arr = [[*map(int, input().split())] for _ in range(r)]
	parr = [[0]*(c+1) for _ in range(r+1)]
	for i in range(1, r+1):
		for j in range(1, c+1):
			parr[i][j] = parr[i-1][j] + parr[i][j-1] - parr[i-1][j-1] + arr[i-1][j-1]

	for k in range(q):
		r1, c1, r2, c2 = map(int, input().split())
		result = (parr[r2][c2] - 
		          parr[r2][c1-1] - 
			      parr[r1-1][c2] + 
				  parr[r1-1][c1-1]) // ((r2-r1+1) * (c2-c1+1))
		print(result)
		
main()
