def solve():
	goal = [1, 1, 2, 2, 2, 8]
	units = [*map(int, input().split())]
	answer = [a-b for a, b in zip(goal, units)]
	print(*answer)

solve()