import sys
input = sys.stdin.readline

def solve():
	n, k, b = map(int, input().split())
	signals = [False] * (n+1)
	for _ in range(b):
		signals[int(input())] = True

	psum = []
	count = 0
	for i in range(n+1):
		count += signals[i]
		psum.append(count)
	
	answer = b
	for i in range(1, n-k+1):
		tmp = psum[i+k]-psum[i]
		if tmp < answer:
			answer = tmp
	
	print(answer)

solve()