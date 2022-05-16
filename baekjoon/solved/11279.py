from heapq import *
from sys import stdin
input = stdin.readline

def solution():
	hq = []
	for _ in range(int(input())):
		x = int(input())
		if x:
			heappush(hq, -x)
		elif hq:
			print(-heappop(hq))
		else:
			print(0)

solution()