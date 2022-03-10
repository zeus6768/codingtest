from itertools import combinations as cm
from sys import stdin

input = stdin.readline
arr = [int(input()) for _ in range(9)]
parr = cm(arr, 7)

for p in parr:
	if sum(p) == 100:
		[print(i) for i in p]