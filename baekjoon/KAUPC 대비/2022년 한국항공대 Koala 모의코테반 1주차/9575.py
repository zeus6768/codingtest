import sys
input = sys.stdin.readline

def solve():
	for _ in range(int(input())):
		input()
		A = [*map(int, input().split())]
		input()
		B = [*map(int, input().split())]
		input()
		C = [*map(int, input().split())]

		lucky = {}
		answer = 0

		for a in A:
			for b in B:
				for c in C:
					tmp = str(a + b + c)
					if len(tmp) == tmp.count('8') + tmp.count('5'):
						if tmp not in lucky:
							lucky[tmp] = 1
							answer += 1
		
		print(answer)

solve()