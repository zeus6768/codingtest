def main():
	n, m = map(int, input().split())
	A = [*map(int, input().split())]

	left, right = 0, 1
	answer = 0
	while right <= n:
		total = sum(A[left:right])
		if total < m:
			right += 1
		elif total > m:
			left += 1
		else:
			right += 1
			answer += 1

	print(answer)

main()