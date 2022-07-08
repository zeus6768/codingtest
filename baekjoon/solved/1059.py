def solve():
	_ = input()
	nums = sorted(map(int, input().split()))
	n = int(input())
	_min, _max = 1, n

	if n in nums:
		print(0)
		exit(0)

	for num in nums:
		if num < n:
			_min = num+1
		else:
			_max = num-1
			break

	answer = (n-_min)*(_max-n+1)+(_max-n)

	print(answer)

solve()