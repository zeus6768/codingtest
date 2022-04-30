import sys
input = sys.stdin.readline

def solution():
	k = int(input())
	arr = []
	for _ in range(k):
		n = int(input())
		arr.append(n) if n else arr.pop()
	print(sum(arr))

solution()