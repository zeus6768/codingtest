import sys; input = sys.stdin.readline

def solve():
	_ = int(input())
	card1 = {*map(int, input().split())}
	_ = int(input())
	card2 = map(int, input().split())
	
	print(" ".join(['1' if c2 in card1 else '0' for c2 in card2]))

solve()