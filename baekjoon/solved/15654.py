def combination(m):
	if m == M:
		print(*answer)
		return
	
	for i in range(N):
		if not answer or answer[-1] <= nums[i]:
			answer.append(nums[i])
			combination(m+1)
			answer.pop()

if __name__ == "__main__":
	N, M = map(int, input().split())
	nums = sorted(map(int, input().split()))
	answer = list()
	combination(0)