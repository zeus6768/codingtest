import sys

def input():
	return sys.stdin.readline()

def solve():
	count = 0
	for i in range(n):
		a = dots[i]
		for j in range(i+1, n-1):
			b = dots[j]
			diff = b-a
			count += find(j, diff)
	print(count)

def find(idx, diff):
	l, r = idx+1, n-1
	while l <= r:
		m = (l+r)//2
		if dots[m]-dots[idx] == diff:
			return 1
		if dots[m]-dots[idx] < diff:
			l = m+1
		if dots[m]-dots[idx] > diff:
			r = m-1
	return 0

if __name__ == "__main__":
	for _ in range(int(input())):
		n = int(input())
		dots = sorted(map(int, input().split()))
		solve()