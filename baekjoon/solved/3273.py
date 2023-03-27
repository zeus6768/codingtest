def solve():
	answer = 0
	l, r = 0, n-1
	while l < r < n:
		if nums[l]+nums[r]==x:
			answer += 1
			l, r = l+1, r-1
		if nums[l] + nums[r] < x:
			l += 1
		if nums[l] + nums[r] > x:
			r -= 1
	print(answer)

if __name__ == "__main__":
	n = int(input())
	nums = sorted(map(int, input().split()))
	x = int(input())
	solve()