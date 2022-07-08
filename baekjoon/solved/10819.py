from itertools import permutations as pmt

def solve():
	n = int(input())
	A = [*pmt(map(int, input().split()))]

	def compute(arr):
		return sum([abs(arr[i]-arr[i+1]) for i in range(n-1)])

	result = max(map(compute, A))
	print(result)

solve()
