import sys
input = sys.stdin.readline

def solve():
	n = int(input())
	deck = [True] + [False] * 26
	for _ in range(n):
		A = [*map(int, input().split())]
		left, right = deck[:13], deck[13:]
		deck = []
		for i in range(len(A)):
			size = A[i]
			if i % 2:
				tmp = left[:size]
				left = left[size:]
			else:
				tmp = right[:size]
				right = right[size:]
			deck += tmp

	print(deck.index(True)+1)

solve()
