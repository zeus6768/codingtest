import sys
input = sys.stdin.readline

def get_germs(s, x, l):
	return s * max(1, x-l)

def solve():
	N, G, K = map(int, input().split())

	ingredients = [[], []]

	for _ in range(N):
		s, l, o = map(int, input().split())
		ingredients[o].append((s, l))

	answer = 0
	left, right = 0, 2*10**9
	while left <= right:
		mid = (left+right)//2
		germs = 0
		for s, l in ingredients[0]:
			germs += get_germs(s, mid, l)
		ingredients[1].sort(key=lambda x: get_germs(x[0], mid, x[1]))
		for i in range(len(ingredients[1])-K):
			s, l = ingredients[1][i]
			germs += get_germs(s, mid, l)
		if germs <= G:
			answer = mid
			left = mid + 1
		else:
			right = mid - 1
	
	print(answer)

solve()