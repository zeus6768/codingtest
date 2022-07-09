import sys; input = sys.stdin.readline

def solve():
	target = input().strip()	
	answer = sum([target in input().strip()*2 for _ in range(int(input()))])
	print(answer)
solve()