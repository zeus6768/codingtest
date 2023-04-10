import sys

def input():
	return sys.stdin.readline()

def solve():
	answer = 0
	cost = costs[0]
	for i in range(N-1):
		if costs[i] < cost:
			cost = costs[i]
		answer += road[i] * cost
	print(answer)

if __name__ == "__main__":
	N = int(input())
	road = tuple(map(int, input().split()))
	costs = tuple(map(int, input().split()))
	solve()