from sys import stdin; input = stdin.readline

def solve():
	for _ in range(int(input())):
		n = int(input())
		s1 = [*map(int, input().split())]
		s2 = [*map(int, input().split())]
		
		dp1 = [0]*(n+2)
		dp2 = [0]*(n+2)

		for i in range(n):
			dp1[i] = max(dp2[i-1]+s1[i], dp2[i-2]+s1[i])
			dp2[i] = max(dp1[i-1]+s2[i], dp1[i-2]+s2[i])

		print(max(dp1[-3], dp2[-3]))

solve()