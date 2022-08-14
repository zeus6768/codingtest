import sys; input = sys.stdin.readline

def solve():

	while True:
		
		n1, n2 = map(int, input().split())
		
		if n1==n2==0:
			break
		elif n2 % n1 == 0:
			print('factor')
		elif n1 % n2 == 0:
			print('multiple')
		else:
			print('neither')
		
solve()