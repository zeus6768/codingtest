import sys
input = sys.stdin.readline

def solve():
	H, x = map(int, input().split())
	d = 10**9+7
	answer = 0
	snowball = 1
	for _ in range(H):
		c = int(input())
		snowball = (snowball*x) % d
		answer += snowball * c
	print(answer % d)

solve()