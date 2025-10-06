import sys

def input():
	return sys.stdin.readline()

N = int(input())
nodes = [0 for _ in range(N+1)]
for i in range(N-1):
	node_1, node_2 = map(int, input().split())
	if node_1 == 1:
		nodes[node_2] = node_1
	elif node_2 == 1:
		nodes[node_1] = node_2
	else:
		...


from collections import deque

cache = set()
