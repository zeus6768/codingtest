from collections import deque
from sys import stdin
input = stdin.readline
p = print

def main():
	n = int(input())
	i_list = [
		'push_front', 'push_back', 
		'pop_front', 'pop_back', 
		'size', 'empty', 
		'front', 'back'
		]
	dq = deque()

	for _ in range(n):
		ins = input().split()
		if ins[0] == i_list[0]:
			dq.appendleft(ins[1])
		elif ins[0] == i_list[1]:
			dq.append(ins[1])
		elif ins[0] == i_list[2]:
			p(dq.popleft()) if dq else p(-1)
		elif ins[0] == i_list[3]:
			p(dq.pop()) if dq else p(-1)
		elif ins[0] == i_list[4]:
			p(len(dq))
		elif ins[0] == i_list[5]:
			p(0) if dq else p(1)
		elif ins[0] == i_list[6]:
			p(dq[0]) if dq else p(-1)
		elif ins[0] == i_list[7]:
			p(dq[-1]) if dq else p(-1)

main()