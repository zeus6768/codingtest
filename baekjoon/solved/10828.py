from sys import stdin
input = stdin.readline

stack = []
n = int(input())
for _ in range(n):
	com = input().split()
	c = com[0]
	if c == 'push':
		stack.append(int(com[1]))
	elif c == 'pop':
		result = stack.pop() if stack else -1
		print(result)
	elif c == 'size':
		result = len(stack)
		print(result)
	elif c == 'empty':
		result = 0 if stack else 1
		print(result)
	elif c == 'top':
		result = stack[-1] if stack else -1
		print(result)