import sys
input = sys.stdin.readline

def solve():
	n, s = map(int, input().split())
	cows = sorted([int(input()) for _ in range(n)])

	answer = 0

	for i in range(n-1):
		for j in range(i+1, n):
			if cows[i] + cows[j] <= s:
				answer += 1

	print(answer)


solve()