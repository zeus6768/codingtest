import sys
input = sys.stdin.readline

def solve():
	n, m = map(int, input().split())
	arr1 = {input().strip() for _ in range(n)}
	arr2 = {input().strip() for _ in range(m)}
	arr3 = sorted(arr1.intersection(arr2))
	print(len(arr3))
	[print(name) for name in arr3]

solve()