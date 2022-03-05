from sys import stdin
input = stdin.readline

def solution(d, r1, r2):
	if (d == 0) and (r1 == r2):
		return -1
	elif d < abs(r1-r2):
		return 0
	elif d == abs(r1-r2):
		return 1
	elif d < r1+r2:
		return 2
	elif d == r1+r2:
		return 1
	else:
		return 0

def main():
	n = int(input())
	for i in range(n):
		x1, y1, r1, x2, y2, r2 = map(int, input().split())
		d = ((x1-x2)**2 + (y1-y2)**2)**0.5
		print(solution(d, r1, r2))

main()