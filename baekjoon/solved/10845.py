from sys import stdin
input = stdin.readline

def queue():
	queue = []
	n = int(input())
	for i in range(n):
		com = input().split()
		c = com[0]
		if c == "push":
			queue.append(int(com[1]))
		elif c == "pop":
			print(queue.pop(0)) if queue else print(-1)
		elif c == "size":
			print(len(queue))
		elif c == "empty":
			print(0) if queue else print(1)
		elif c == "front":
			print(queue[0]) if queue else print(-1)
		elif c == "back":
			print(queue[-1]) if queue else print(-1)

queue()
