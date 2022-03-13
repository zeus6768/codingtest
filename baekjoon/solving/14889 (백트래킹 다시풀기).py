from sys import stdin
input = stdin.readline

# 풀이1. combinations


# 풀이2. 재귀함수
def solution(idx, num):
	global res
	if num == n // 2:
		team_a, team_b = 0, 0
		for i in range(n):
			for j in range(i+1, n):
				if team[i] == team[j]:
					if team[i] == 0:
						team_a += arr[i][j] + arr[j][i]
					else:
						team_b += arr[i][j] + arr[j][i]
		res = min(res, abs(team_a - team_b))
	
	for i in range(idx+1, n):
		team[i] = 1
		solution(i, num+1)
		team[i] = 0

res = float("inf")
n = int(input())
arr = [[*map(int, input().split())] for _ in range(n)]	
team = [0] * n

solution(0, 0)

print(res)
