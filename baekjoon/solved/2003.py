def solve():
	n, m = map(int, input().split())
	nums = [*map(int, input().split())]

	answer = 0
	left, right = 0, 0

	while right < n:
		_sum = sum(nums[left:right+1])
		if _sum == m:
			answer += 1
			right += 1
		elif _sum < m:
			right += 1
		elif _sum > m:
			left += 1
	
	print(answer)

solve()