from sys import stdin
from collections import deque
input = stdin.readline

def solution():
	for _ in range(int(input())):
		p = input().strip()
		input()
		arr = deque(input().strip('[]\n').split(','))
		order = True
		error = False
		for inst in p:
			if inst == 'R':
				order = not order
			elif arr and arr[0]:
				if order:
					arr.popleft()
				else:
					arr.pop()
			else:
				error = True
				break
		print('error' if error else "[" + ",".join(arr if order else reversed(arr)) + "]")

solution()
