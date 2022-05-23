import sys
input = sys.stdin.readline

def solution():
	n, k = map(int, input().split())
	막걸리 = [int(input()) for _ in range(n)]
	answer = 0
	l, r = 0, max(막걸리)
	while l <= r:
		m = (l+r) // 2
		분배 = sum(map(lambda x: x//m if m else 1, 막걸리))
		if 분배 >= k:
			answer = max(answer, m)
			l = m + 1
		else:
			r = m - 1
	print(answer)

solution()
