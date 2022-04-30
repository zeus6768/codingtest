import sys
input = sys.stdin.readline

def solution():
	n, p = map(int, input().split())
	w, l, g = map(int, input().split())
	info = {}
	for _ in range(p):
		name, result = input().split()
		info[name] = result
	
	score = 0
	for _ in range(n):
		team = input().strip()
		if team in info:
			score += w if info[team] == 'W' else -l
		else:
			score -= l
		if score >= g:
			print("I AM NOT IRONMAN!!")
			exit()
		elif score <= 0:
			score = 0
	print("I AM IRONMAN!!")

solution()

## correct