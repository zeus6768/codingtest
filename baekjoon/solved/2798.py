from sys import stdin
input = stdin.readline

def combination(card_list):
	size = len(card_list)
	result = []
	for i in range(size):
		for j in range(i+1, size):
			for k in range(j+1, size):
				result.append((card_list[i], card_list[j], card_list[k]))
	return result

def sum_under_m(combination, m):
	return [sum(c) for c in combination if sum(c) <= m]

def main():
	n, m = map(int, input().split())
	cards = list(map(int, input().split()))
	combi = combination(cards)
	sums = sum_under_m(combi, m)
	return max(sums)

print(main())