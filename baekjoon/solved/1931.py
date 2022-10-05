import sys
input = sys.stdin.readline

def solve():
	n = int(input())
	schedule = [[*map(int, input().split())] for _ in range(n)]
	schedule.sort(key=lambda x: (x[1], x[0]))

	answer = 0
	prev_end = 0

	for start, end in schedule:
		if prev_end <= start:
			answer += 1
			prev_end = end
	
	print(answer)

solve()