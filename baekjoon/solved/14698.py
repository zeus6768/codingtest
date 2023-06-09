from heapq import heapify, heappop, heappush
import sys

def input():
	return sys.stdin.readline()

def study():
	answer = 1
	while len(slimes) > 1:
		slime_1 = heappop(slimes)
		slime_2 = heappop(slimes)
		slime_3 = slime_1 * slime_2
		answer = answer * slime_3 % DIVIDE
		heappush(slimes, slime_3)
	print(answer)

if __name__ == "__main__":

	DIVIDE = 1_000_000_007

	T = int(input())

	for _ in range(T):
		N = int(input())
		slimes = list(map(int, input().split()))
		heapify(slimes)
		study()