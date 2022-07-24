from sys import stdin
input = stdin.readline

def main():
	n, m = map(int, input().split())
	cards = list(map(int, input().split()))
	
	answer = 0
	for i in range(n):
		for j in range(i+1, n):
			for k in range(j+1, n):
				_sum = sum([cards[i], cards[j], cards[k]])
				if _sum <= m:
					if answer < _sum:
						answer = _sum

	print(answer)

main()