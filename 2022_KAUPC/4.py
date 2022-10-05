import sys
input = sys.stdin.readline

def solve():
	N, K = map(int, input().split())
	cost = [*map(int, input().split())]
	
	dp = [[float('inf')]*N for _ in range(2)]
	

solve()