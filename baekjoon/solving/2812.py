def solve():
    
	N, K = map(int, input().split())
	number = input()

	status = [True] * N

	i, j = 0, 1
	while K > 0:

		while K > 0 and i < N and status[i] and K+i == N:
			status[i] = False
			K -= 1
			i += 1

		while K > 0 and 0 <= i < j < N and status[i] and status[j] and number[i] < number[j]:
			status[i] = False
			K -= 1
			i -= 1

		if i < j:
			i += 1
		else:
			j += 1

	answer = "".join([number[i] for i in range(N) if status[i]])

	print(answer)
		
	
solve()