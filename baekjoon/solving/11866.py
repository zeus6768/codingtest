# 풀이 1
def main():
	n, k = map(int, input().split())
	tf = [True] * n
	result = []
	nums = range(n)
	idx, cnt = k - 1, k
	while True in tf:
		if tf[idx] and cnt == k:
			result.append(str(nums[idx] + 1))
			tf[idx] = False
			cnt = 0
		elif not tf[idx]:
			cnt -= 1
		cnt += 1
		idx = (idx+1) % n
	print('<'+", ".join(result)+'>')

[1, 2, 3, 4, 5, 6, 7]


# 풀이 2
def solve():
	n, k = map(int, input().split())
	nums = [*range(1, n+1)]
	ans = []
	idx = 0

	while nums:
		idx = (idx+k-1) % len(nums)
		ans.append(nums[idx])
		del nums[idx]

	print('<'+str(ans)[1:-1]+'>')
solve()