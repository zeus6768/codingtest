import sys
input = sys.stdin.readline

def solve():
	n = int(input())
	room = [[*map(int, input().split())] for _ in range(n)]
	
	com_num = sum([sum(r) for r in room])

	threshold = -(-com_num//2)

	def count(time):
		result = 0
		for i in range(n):
			for j in range(n):
				if 0 < room[i][j] <= time:
					result += room[i][j]
				elif room[i][j] > time:
					result += time
		return result
	
	l, r = 0, 10_000_000
	while l <= r:
		mid = (l+r)//2
		c = count(mid)

		if c < threshold:
			l = mid + 1
		else:
			answer = mid
			r = mid - 1
	
	print(answer)
		
solve()