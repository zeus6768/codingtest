from sys import stdin
from heapq import *
input = stdin.readline

def solution():
	n = int(input())
	arr = []
	for _ in range(n):
		op = int(input())
		if op:
			heappush(arr, op)
		elif arr:
			print(heappop(arr))
		else:
			print(0)

solution()