import sys
input = sys.stdin.readline

def solve():
	s, c = map(int, input().split())
	pa = [int(input()) for _ in range(s)]
	
	answer = 0
	l, r = 1, max(pa)

	while l <= r:
		count = 0
		leftover = 0
		mid = (l+r)//2

		for p in pa:
			count += p//mid
			leftover += p%mid

		if count < c:
			r = mid - 1
		elif count > c:
			l = mid + 1
			answer = mid*(count-c)
		else:
			l = mid + 1
			answer = leftover

	print(answer)


solve()