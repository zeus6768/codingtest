import sys
input = sys.stdin.readline

def solution1():
	n = int(input())

	if n < 2:
		print(n)
	else:
		a, b = 0, 1
		for i in range(2, n+1):
			a, b = b, (a+b) % 1000000007
		print(b)

solution1()