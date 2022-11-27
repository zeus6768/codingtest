import sys
input = sys.stdin.readline

def solve():
	_, M = map(int, input().split())
	locations = [*map(int, input().split())]

	for _ in range(M):
		P, C = map(int, input().split())
		
		answer = 0

		for location in locations:
			if location in range(P-C, P+C+1):
				answer += 1
		
		print(answer)


solve()