from sys import stdin
from heapq import heappop, heappush

def input():
	return stdin.readline()

def main():
	t = int(input())
	for _ in range(t):
		EXISTS = dict()
		max_heap, min_heap = [], []
		k = int(input())
		for _ in range(k):
			I, n = input().split()
			n = int(n)
			if I == 'I':
				insert(n, max_heap, min_heap, EXISTS)
			if I == 'D':
				delete(n, max_heap, min_heap, EXISTS)
		clear(max_heap, min_heap, EXISTS)
		if not any(EXISTS.values()):
			print("EMPTY")
		else:
			print(-max_heap[0], min_heap[0])

def insert(n, max_heap, min_heap, EXISTS):
	heappush(max_heap, -n)
	heappush(min_heap, n)
	add_count(n, EXISTS)

def delete(n, max_heap, min_heap, EXISTS):
	clear(max_heap, min_heap, EXISTS)
	if is_max_valid(max_heap, EXISTS) and n == 1:
		v = -heappop(max_heap)
		EXISTS[v] -= 1
	if is_min_valid(min_heap, EXISTS) and n == -1:
		v = heappop(min_heap)
		EXISTS[v] -= 1

def clear(max_heap, min_heap, EXISTS):
	while max_heap and not EXISTS[-max_heap[0]]:
		heappop(max_heap)
	while min_heap and not EXISTS[min_heap[0]]:
		heappop(min_heap)

def is_max_valid(heap, EXISTS):
	return heap and -heap[0] in EXISTS and EXISTS[-heap[0]]

def is_min_valid(heap, EXISTS):
	return heap and heap[0] in EXISTS and EXISTS[heap[0]]

def add_count(n, EXISTS):
	if n in EXISTS:
		EXISTS[n] += 1
	else:
		EXISTS[n] = 1

main()