def solve():
	n = int(input())
	nums = [*map(int, input().split())]

	_min = 10e9
	l, r = 0, n-1

	while l < r:
		_sum = nums[l] + nums[r]
		if abs(_sum) < _min:
			al, ar = l, r
			_min = abs(_sum)
		
		if _sum > 0:
			r -= 1
		elif _sum < 0:
			l += 1
		else:
			break
	
	print(nums[al], nums[ar])

solve()