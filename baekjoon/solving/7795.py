import sys
input = sys.stdin.readline

def solve():
	for _ in range(int(input())):
		n, m = map(int, input().split())
		A = sorted(map(int, input().split()), reverse=True)
		B = sorted(map(int, input().split()), reverse=True)

		answer = 0
		a, b = 0, 0
		while a < n and b < m :
			if A[a] <= B[b]:
				b += 1
			else:
				answer += m - b
				a += 1

		print(answer)

solve()