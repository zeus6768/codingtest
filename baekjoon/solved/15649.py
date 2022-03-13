from sys import stdin
input = stdin.readline

# 풀이1. permutations
def solution1():
	from itertools import permutations as pm

	n, m = map(int, input().split())
	[print(*a) for a in pm([i+1 for i in range(n)], m)]

# 풀이2. 재귀함수
def solution2():
	n, m = map(int, input().split())
	ans = []

	def go():
		if len(ans) == m:
			print(*ans)
			return
		for i in range(1, n+1):
			if i not in ans:
				ans.append(i)
				go()
				ans.pop()

	go()

solution2()