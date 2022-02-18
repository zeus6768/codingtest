import sys
input = sys.stdin.readline

def solution():
	a, b, c = map(int, input().split())
	n = int(input())
	info, result, team_score = [], [], 0
	[info.append(list(map(int, input().split()))) for _ in range(3 * n)]
	for i, score in enumerate(info):
		member_score = a*score[0] + b*score[1] + c*score[2]
		if i % 3 == 0:
			team_score = 0
			team_score += member_score
		elif i % 3 == 2:
			team_score += member_score
			result.append(team_score)
		else:
			team_score += member_score
	print(max(result))

solution()