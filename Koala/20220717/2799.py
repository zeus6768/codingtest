from curses import window
import sys
input = sys.stdin.readline

def b_type(windows):
	if windows[0] == '....':
		return 0
	elif windows[0] == '****' and windows[1] == '....':
		return 1
	elif windows[1] == '****' and windows[2] == '....':
		return 2
	elif windows[2] == '****' and windows[3] == '....':
		return 3
	elif windows[3] == '****':
		return 4

def solve():
	m, n = map(int, input().split())
	apart = [input().strip() for _ in range(5*m+1)]
	answer = [0] * 5

	for i in range(m):
		for j in range(n):
			wins = [apart[5*i+1+k][5*j+1:5*(j+1)] for k in range(4)]
			answer[b_type(wins)] += 1

	print(*answer)
	

solve()
