from sys import stdin, stdout
import heapq

input = stdin.readline
print = stdout.write

def solve():
	n, m = map(int, input().split())
	ice = list(map(int, input().split()))
	
	ice_cream = [(-ice[i], i+1) for i in range(n)]
	heapq.heapify(ice_cream)

	for _ in range(m):
		eat = heapq.heappop(ice_cream)
		print(str(eat[1]) + "\n")

	
solve()
