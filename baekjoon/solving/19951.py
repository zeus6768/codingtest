import sys
input = sys.stdin.readline

def main():
	n, m = map(int, input().split())
	ground = [*map(int, input().split())]

	temp = [0] * (n+2)
	for i in range(m):
		a, b, k = map(int, input().split())
		temp[a] += k
		temp[b+1] -= k
	
	psum = [0] * (n+2)
	for j in range(1, n+1):
		psum[j] = psum[j-1] + temp[j]

	answer = [0] * n
	for k in range(n):
		answer[k] = psum[k+1] + ground[k]
	
	print(*answer)

main()