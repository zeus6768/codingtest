import sys
input = sys.stdin.readline

def solve():
	for _ in range(int(input())):
		n, m, k = map(int, input().split())
		money = [*map(int, input().split())]

		if n == m:
			if sum(money) < k:
				print(1)
			else:
				print(0)
			continue

		money.extend(money)
		csum = [0]
		[csum.append(csum[i]+money[i]) for i in range(n+m)]
		answer = 0

		for i in range(n):
			if csum[i+m] - csum[i] < k:
				answer += 1
		
		print(answer)


solve()