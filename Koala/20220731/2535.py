# 1번
import sys
input = sys.stdin.readline

def solve():
	n = int(input())
	students = [[*map(int, input().split())] for _ in range(n)]
	students = sorted(students, key=lambda x: -x[2])

	answer = [students[0], students[1]]
	for i in range(2, n):
		if students[0][0] == students[1][0] != students[i][0]:
			answer.append(students[i])
			break
		elif students[0][0] != students[1][0]:
			answer.append(students[i])
			break

	[print(*a[:2]) for a in answer]

solve()