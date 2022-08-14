import heapq
import sys
input = sys.stdin.readline

def solve():
	n = int(input())
	cards = [int(input()) for _ in range(n)]

	heapq.heapify(cards)

	tmp, res, answer = 0, 0, 0
	while cards:
		if tmp:
			res = tmp + heapq.heappop(cards)
			heapq.heappush(cards, res)
			answer += res
			tmp = 0
		else:
			tmp = heapq.heappop(cards)

	print(answer)

solve()