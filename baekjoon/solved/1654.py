import sys
input = sys.stdin.readline

def solve():
	k, n = map(int, input().split())
	lans = [int(input().strip()) for _ in range(k)]

	answer = 0
	l, r = 0, 2**31-1

	while l <= r:
		mid = (l+r) // 2
		cnt = sum([lan//mid for lan in lans])
		if cnt < n:
			r = mid -1
		else:
			l = mid + 1
			answer = mid

	print(answer)


solve()