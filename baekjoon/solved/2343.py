def solve():
	_, m = map(int, input().split())
	bluerays = list(map(int, input().split()))

	answer = float('inf')
	l, r = 0, 10000*m

	while l <= r:
		mid = (l+r)//2
		record, count = mid, 1

		for b in bluerays:
			if record < b:
				record = mid
				count += 1
			record -= b
		
		if m < count or mid < max(bluerays):
			l = mid + 1
		else:
			answer = min(answer, mid)
			r = mid - 1

	print(answer)


solve()