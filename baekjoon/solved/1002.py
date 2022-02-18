from sys import stdin
input = stdin.readline

n = int(input())
for i in range(n):
	x1, y1, r1, x2, y2, r2 = map(int, input().split())
	d = ((x1-x2)**2 + (y1-y2)**2)**0.5
	if x1==x2 and y1==y2 and r1==r2:
		print(-1)
	elif r1 + r2 > d:
		print(2)
	elif r1 + r2 == d:
		print(1)
	elif r1 + r2 < d:
		print(0)