import sys
input = sys.stdin.readline

def solution():
	n = int(input())
	table = [[*map(int, input().split())] for _ in range(n)]

	team = [False] * n
	answer = [float('inf')]

	def compare(idx, size):
		if size == n//2:
			team1, team2 = 0, 0
			for i in range(n):
				for j in range(i+1, n):
					if team[i] == team[j]:
						if team[i]:
							team1 += table[i][j] + table[j][i]
						else:
							team2 += table[i][j] + table[j][i]
			answer[0] = min(answer[0], abs(team1-team2))

		for i in range(idx+1, n):
			team[i] = True
			compare(i, size+1)
			team[i] = False

	compare(0, 0)
	print(*answer)

solution()