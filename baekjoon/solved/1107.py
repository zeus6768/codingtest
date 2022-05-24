import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def solution():
	n = input().strip()
	m = int(input())
	broken = input().split() if m else []
	buttons = [str(i) for i in range(10) if str(i) not in broken]

	nums = []
	def get_num(number):
		if len(number) == len(n): 
			nums.append(number)
			return
		[get_num(number+b) for b in buttons]

	if 98 <= int(n) <= 103:
		print(abs(100 - int(n)))
	else:
		get_num("")
		channel, tmp = '100', 500000
		for num in nums:
			diff = abs(int(num) - int(n))
			if diff < tmp:
				tmp = diff
				channel = num
		answer = len(channel) + abs(int(channel)-int(n))
		print(answer)

solution()