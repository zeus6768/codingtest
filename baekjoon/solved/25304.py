import sys
input = sys.stdin.readline

def solve():
	x = int(input())
	n = int(input())
	
	for _ in range(n):
		a, b = map(int, input().split())
		x -= a * b
	
	print("No") if x else print("Yes")

solve()