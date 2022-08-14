import sys
input = sys.stdin.readline

def solve():
	n, m = map(int, input().split())
	nums = [list(map(int, input().split())) for _ in range(n)]

	psum = [[0]*(n+1) for _ in range(n+1)]

	for i in range(1, n+1):
		for j in range(1, n+1):
			psum[i][j] = psum[i-1][j] + psum[i][j-1] - psum[i-1][j-1] + nums[i-1][j-1]
	
	for _ in range(m):
		x1, y1, x2, y2 = map(int, input().split())
		answer = psum[x2][y2] - psum[x2][y1-1] - psum[x1-1][y2] + psum[x1-1][y1-1]
		print(answer)

solve()