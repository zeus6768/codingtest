from collections import deque
from sys import stdin
input = stdin.readline

def solve():
	n = int(input())
	
	queue = deque()

	for _ in range(n):
		op = input().strip()

		if 'push' in op:
			value = op.split()[1]
			queue.append(value)
		elif 'pop' in op:
			value = queue.popleft() if queue else -1
			print(value)
		elif 'size' in op:
			print(len(queue))
		elif 'empty' in op:
			print(1) if len(queue)==0 else print(0)
		elif 'front' in op:
			print(queue[0]) if queue else print(-1)
		elif 'back' in op:
			print(queue[-1]) if queue else print(-1)

solve()