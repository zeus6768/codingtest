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
		if len(n)-1 <= len(number): 
			nums.append(number)
			if len(number) == len(n) + 1:
				return
		[get_num(number+b) for b in buttons]

	if 98 <= int(n) <= 103:
		print(abs(100 - int(n)))
	else:
		get_num("")
		diff = abs(100-int(n))
		for num in nums:
			if num:
				tmp = abs(int(num) - int(n)) + len(num)
				if tmp < diff:
					diff = tmp
		print(diff)

solution()