import sys
input = sys.stdin.readline

def solve():
	n, q = map(int, input().split())
	A = [*map(int, input().split())]
	
	psum, ppow = [0], [0]
	for i in range(n):
		psum.append(psum[i] + A[i])
		ppow.append(ppow[i] + A[i]**2)

	for _ in range(q):
		l, r = map(int, input().split())
		power_of_sum = (psum[r] - psum[l-1])**2
		sum_of_powers = ppow[r] - ppow[l-1]
		result = (power_of_sum-sum_of_powers)//2
		print(result)

solve()