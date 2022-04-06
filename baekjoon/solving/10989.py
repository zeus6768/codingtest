input = lambda: __import__('sys').stdin.readline().strip()

def solution():
	nums = {}
	for i in range(int(input())):
		n = int(input())
		if n in nums:
			nums[n] += 1
		else:
			nums[n] = 1
	for i in sorted(nums):
		for j in range(nums[i]):
			print(i)

solution()