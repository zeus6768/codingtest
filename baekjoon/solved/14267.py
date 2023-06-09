import sys

def input():
	return sys.stdin.readline()

def dfs():
	stack = [(0, 0)]
	while stack:
		i, w = stack.pop()
		answer[i] += w
		for staff in staffs[i]:
			stack.append((staff, compliments[staff]+w))

if __name__ == "__main__":
	n, m = map(int, input().split())
	bosses = tuple(map(int, input().split()))
	
	answer = [0] * n

	staffs = [[] for _ in range(n+1)]
	[staffs[bosses[i]-1].append(i) for i in range(n) if bosses[i] != -1]

	compliments = [0] * n
	for _ in range(m):
		i, w = map(int, input().split())
		compliments[i-1] += w

	dfs()
	print(*answer)