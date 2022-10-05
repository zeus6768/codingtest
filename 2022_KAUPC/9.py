from collections import deque
import sys
input = sys.stdin.readline

def solve():
	n, m = map(int, input().split())
	A = [[*map(int, input().split())] for _ in range(n)]
	A.sort(key=lambda x: x)

	return


solve()