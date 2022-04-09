input = __import__('sys').stdin.readline

def main():
	n = int(input())
	nums = [0] * 10001
	for _ in range(n):
		idx = int(input())
		nums[idx] += 1
	for i in range(10001):
		if nums[i]:
			for _ in range(nums[i]):
				print(i)

main()