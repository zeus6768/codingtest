def main():
	n = int(input())
	W = sorted(map(int, input().split()))

	left, right = 0, 2*n-1
	answer = 200000
	for i in range(n):
		g = W[left+i] + W[right-i]
		answer = min(answer, g)

	print(answer)

main()