def solve():
	n, s = map(int, input().split())
	nums = [*map(int, input().split())]

	csum = [0]
	[csum.append(nums[i] + csum[i]) for i in range(n)]

	answer = float('inf')
	l, r = 0, 1

	while r <= n:
		num = csum[r] - csum[l]
		if num < s:
			r += 1
		else:
			if r-l <= answer:
				answer = r-l
			l += 1

	print(answer) if answer != float('inf') else print(0)


solve()