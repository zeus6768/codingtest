import sys
input = sys.stdin.readline


def solution():
	_, m = map(int, input().split())
	times = [*map(int, input().split())]
	
	b = 0
	l, r = 0, 10**12
	result = 0
	while l < r:
		mid = (l+r) // 2
		b = sum([mid//t for t in times])
		if b < m:
			l = mid + 1
		else:
			result = mid
			r = mid
	
	print(result)


solution()
