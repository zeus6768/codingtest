import sys

def input():
	return sys.stdin.readline().strip()

def solve():
	for i in range(len(items)):

		...

def combinations(n, k):
	...
	
def factorial(n):
	total = 1
	for i in range(2, n+1):
		total *= i
	return total

if __name__ == "__main__":
	items = dict()
	for _ in range(int(input())):
		n = int(input())
		item, category = input().split()
		if category in items:
			items[category].append(item)
		else:
			items[category] = [item]