import sys
input = sys.stdin.readline

def solve():
	n, k = map(int, input().split())
	A = [int(input()) for _ in range(n)]

	answer = 0
	while k:
		for i in range(n):
			coin_type = A[n-i-1]
			num_of_coins = k // coin_type
			if num_of_coins:
				answer += num_of_coins
				k %= coin_type
				break

	print(answer)

solve()