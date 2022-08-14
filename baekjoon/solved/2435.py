def solve():
	n, k = map(int, input().split())
	temp = list(map(int, input().split()))
	
	csum = [0]
	for i in range(1, n+1):
		csum.append(csum[i-1] + temp[i-1])

	_max = -float('inf')
	for i in range(n-k+1):
		tmp = csum[i+k] - csum[i]
		if _max < tmp:
			_max = tmp

	print(_max)

solve()