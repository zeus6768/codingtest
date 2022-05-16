from sys import stdin
from heapq import *
input = stdin.readline

def solution():
	hq = []
	for _ in range(int(input())):
		x = int(input())
		if x:
			heappush(hq, (abs(x), x))
		elif hq:
			print(heappop(hq)[1])
		else:
			print(0)

solution()