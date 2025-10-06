import sys

def input():
	return sys.stdin.readline().strip()

cursor_left = list(input())
cursor_right = list()
M = int(input())

commands = {
	'L': lambda l, r, _='': r.append(l.pop()) if l else None, 
	'D': lambda l, r, _='': l.append(r.pop()) if r else None, 
	'B': lambda l, _='', __='': l.pop() if l else None, 
	'P': lambda l, _, c: l.append(c)
}

for _ in range(M):
	c, *char = input().split()
	commands[c](cursor_left, cursor_right, *char)

print("".join(cursor_left + list(reversed(cursor_right))))