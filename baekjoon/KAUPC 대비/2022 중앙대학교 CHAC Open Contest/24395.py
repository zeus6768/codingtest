import sys
input = sys.stdin.readline

def solve():
	N, M = map(int, input().split())

	diseases = [[*map(int, input().split())] for _ in range(M)]
	students = [[*map(int, input().split())] for _ in range(N)]

	for i, student in enumerate(students):

		...