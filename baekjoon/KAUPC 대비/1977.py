def solve():
	M = int(input())
	N = int(input())

	answer = []
	i = 1
	while True:
		j = i**2
		if M <= j <= N:
			answer.append(j)
		elif j > N:
			break
		i += 1

	if answer:
		print(sum(answer))
		print(min(answer))
	else:
		print(-1)

solve()