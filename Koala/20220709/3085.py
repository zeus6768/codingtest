import sys; input = sys.stdin.readline

def solve():
	n = int(input())
	candies = [list(input().strip()) for _ in range(n)]

	def count():
		_max = 0

		for i in range(n):
			count, prev = 0, ''
			for j in range(n):
				if candies[i][j] == prev:
					count += 1
				else:
					count = 1
				prev = candies[i][j]
				_max = max(_max, count)

		for i in range(n):
			count, prev = 0, ''
			for j in range(n):
				if candies[j][i] == prev:
					count += 1
				else:
					count = 1
				prev = candies[j][i]
				_max = max(_max, count)

		return _max


	MAX = 0
	# 가로
	for i in range(n):
		for j in range(n-1):
			# 바꾸고
			candies[i][j], candies[i][j+1] = candies[i][j+1], candies[i][j]
			# 개수 세고
			MAX = max(MAX, count())
			# 원위치
			candies[i][j], candies[i][j+1] = candies[i][j+1], candies[i][j]

	# 세로
	for i in range(n):
		for j in range(n-1):
			candies[j][i], candies[j+1][i] = candies[j+1][i], candies[j][i]
			MAX = max(MAX, count())
			candies[j][i], candies[j+1][i] = candies[j+1][i], candies[j][i]

	print(MAX)

solve()
